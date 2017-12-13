1 description
--------------

### 1.1 Introduction

WLANs can be operated in two different modes according to the needs of an operator and the hardware equipment available. In ad hoc mode, two or more mobile devices equipped with a WLAN card communicate directly with each other. Since WLANs can be set up and configured independently in ad-hoc mode, without fixed infrastructure, and thus can establish a fully meshed parallel network infrastructure, it is not recommended to operate WLANs in ad hoc mode in an environment to be protected. This will not be considered further below. The present implementation notes assume that all access points (access points) are centrally administered and not operated in ad hoc mode.

For the implementation notes, the following three fictitious scenarios are used.

1st scenario

* The information is not classified as confidential.
* Access Points may be administered via a cloud infrastructure.
* Users use the provided WLAN infrastructure for telephony.
2nd scenario

* The information is partially classified as confidential.
* Access points must not be administered via a cloud infrastructure.
* Users use the provided WLAN infrastructure for telephony.
* Users can also access internal collaboration and document management systems via the WLAN infrastructure.
3rd scenario

* The information is sometimes classified as strictly confidential.
* Access points must not be administered via a cloud infrastructure.
* Users use the provided WLAN infrastructure for telephony.
* Users can also access the institution's internal collaboration and document management systems, financial data, or critical systems via the WLAN infrastructure.
### 1.2 Life cycle

** planning and conception **

All desired usage scenarios and functions as well as the associated regulatory requirements should be incorporated into the design of the future WLAN infrastructure in the planning and design phase. The basis for this is a sophisticated WLAN strategy (see NET.2.1.M1 * Definition of a strategy for the use of WLANs *). The existing processes should be analyzed to see if they have possible interfaces to the processes of the future WLAN infrastructure, and if necessary they should be updated. In addition, it should be examined whether the functions that the WLAN infrastructure entails are compatible with the business, security and data protection regulations.

In addition to the strategy, the selection of the correct WLAN standard and the associated crypto-method (see NET.2.1.M2 * Selection of a suitable WLAN standard * and NET.2.1.M3 * Selection of suitable crypto procedures for WLAN *) are important topics already must be addressed in the planning phase.

All decisions made regarding security settings, selected WLAN standards, and the rules for the administration of the WLAN should be written down in a WLAN security policy (see NET.2.1.M10 * Creation of a security policy for the operation of WLANs *). Worth knowing about WLANs can be found under "Worth to know" in chapter 3.1.1 * Introduction to WLAN basic terms *.

**Procurement**
When selecting the WLAN components, the measure NET.2.1.M11 * Suitable selection of WLAN components * must be used. As standards, protocols and integrated security mechanisms continue to evolve, WLANs are undergoing rapid change. This means that the WLAN infrastructure itself or individual components need to be migrated more frequently. For migration phases of individual WLAN components or even entire WLAN areas, necessary WLAN migration steps must be carefully planned and ideally verified in a proof of concept prior to the actual migration.

**Implementation**

In order to achieve the maximum possible transfer rates, it does not matter at what point the access points are positioned in the room (see NET.2.1.M4 * Appropriate Installation of Access Points *). The WLAN components or the WLAN management solution must always be configured according to the internal security guidelines during installation (see NET.2.1.M5 * Secure basic configuration of the access points * and NET.2.1.M6 * Secure configuration of the WLAN clients * ). If WLANs are connected to the possibly already existing wired infrastructure, the transition between WLANs and LANs must be protected according to the higher protection requirements (see NET.2.1.M7 * Structure of a Distribution System * and NET.2.1.M9 * Secure Connection of WLANs to a LAN *).

In order to avoid misconfigurations or incorrect operation and to point out possible dangers that may arise when WLANs are operated improperly, those responsible should be adequately trained and sensitized. Further information can be found in the module ORP.3 * Information security and training *.

**Business**

If the WLAN has been put into operation and all WLAN managers have been adequately trained, regular audits (see NET.2.1.M14 * Regular audits of the WLAN components *) must ensure that all security settings made are always up-to-date and that these settings also apply , A key management for the used cryptographic keys is indispensable, in order to secure the communication in WLANs (see CON.1 * Crypto concept *). If a WLAN management solution (see NET.2.1.M12 * Use of a suitable WLAN management solution *) is used, the keys, settings and the WLAN components themselves can be managed centrally from one location.

** ** segregation

If WLAN components are taken out of operation, configuration settings must be removed and reset to default values. Further information can be found in the POU CON.6 * Delete and Destroy *.

** Emergency Preparedness **

If attacks on WLANs have been detected, the persons responsible for the WLANs must know how to behave (see NET.2.1.M8 * Behavioral rules for WLAN security incidents *). This results in an emergency plan, which steps are necessary and which persons are to be informed when a security incident occurs.

2 measures
-----------

The following are specific implementation instructions in the "WLAN operation" area.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### NET.2.1.M1 Definition of a strategy for the use of WLANs [Head IT]

If the following questions are answered, the basic principles of the WLAN strategy can be deduced from this.

* In which areas (organizational as well as spatial) should a WLAN infrastructure be used?
* What potential does the use of a WLAN infrastructure offer?

 
+ Which aspects of mobility are made possible by WLANs?
+ Which functions or applications should be provided or supported by WLAN usage (eg voice over WLAN, media broadcasting, collaboration, videoconferencing, guest access / hotspot, integration of mobile devices, client network segmentation)?
+ Which business processes can be optimized by using WLANs?


 
* What is the security risk of using a WLAN infrastructure or the risk of losing data / information via WLANs?
* Which legal regulations must be adhered to?
* Which classified data / information should not be transmitted without additional cryptographic protection mechanisms?
* Who is responsible for running the WLAN infrastructure?

 
+ Is the WLAN infrastructure administered externally?
+ Can the WLAN infrastructure be administered cloud-based?


 
* What requirements are placed on the availability of the WLAN infrastructure?
#### NET.2.1.M2 Selection of a suitable WLAN standard [planner]

As part of the WLAN design, which follows the documented strategic requirements, potentially disruptive systems near the future location of access points must be identified and evaluated. If microwaves are operated near access points or other IT systems, interference may occur. Possible sources of interference include Bluetooth transmitters, power lines, cordless phones (DECT) or LCD monitors, as well as the building material itself.

If the requirements for the procurement of hardware and software are put together, it must be ensured that the authentication is implemented according to the standard IEEE 802.11i-2004 or later.

To avoid brute force attacks on Wi-Fi passwords, the WLAN infrastructure should support the IEEE 802.11s standard. This standard uses Simultaneous Authentication of Equals (SAE) to define that the actual password is no longer transmitted over the radio channel. As a result, the usual attacks can be effectively countered by recording a connection setup followed by a brute-force attack on the WLAN password. The IEEE 802.11ac standard defines how management frames should be protected by means of protected management frames (PMF) against counterfeit deassociation packets of an attacker. However, in order to use PMF effectively, the terminal must also support the IEEE 802.11ac standard.

Table 1 shows various authentication options for the three fictional scenarios.

Table: WLAN authentication methods

Table 2 gives an overview of the supported IEEE 802.1X EAP solutions based on the listed terminals or their operating systems. It does not list all variants and does not show the value of the individual systems. EAP-TLS or EAP-AKA should be used instead of EAP-PEAP, EAP-TTLS or EAP-SIM. However, as EAP-PEAP and EAP-TTLS are still in widespread use, they are still listed in the table.

Table: WLAN EAP authentication variants depending on the type of operating system

If EAP-TTLS is used, cryptographically secured authentication methods must be used. For the IEEE 802.1X-based authentication of smartphones and tablets to the WLAN infrastructure, EAP-SIM / EAP-AKA is also available.

#### NET.2.1.M3 Selection of suitable crypto procedures for WLAN [Planner]

In order to operate WLANs securely, communication must be cryptographically secured via Wi-Fi Protected Access 2 (WPA2). Easily compromised cryptographic methods may no longer be used. If WEP or WPA are still in use, a migration to WPA2 planned for this should be updated.

If WPA2 is used with pre-shared keys (WPA2-PSK), a complex key with a minimum length of 20 characters must be configured. Since the key needs to be replaced regularly, this method is economically viable only for small Wi-Fi installations. In addition, care must be taken with WPA2-PSK that the German umlauts and special control characters can not be used.

#### NET.2.1.M4 Appropriate installation of access points [building services]
To prevent tampering with access points, they must be housed in sturdy enclosures that can be wall-mounted inside a building. In addition, an access point against simple theft z. B. be secured by a Kensington lock on the housing itself. For Wi-Fi accessibility reasons, access points should not be placed in false ceilings or suspended ceilings unless external antennas are used. This also applies to the attachment of metal cages to protect access points, since they also have an essential influence on the transmission quality and throughput of a WLAN, in particular if beamforming technology according to the IEEE 802.11ac standard is used.

The optimal locations of the access points should be determined by an illumination measurement.

If external areas are supplied, external installations (antennas and, if applicable, access points) must be adequately protected against the effects of the weather, electrical discharges and unauthorized access. Outside of buildings, access points should be avoided.

#### NET.2.1.M5 Secure base configuration of access points

Preset SSIDs, access passwords or cryptographic keys must be changed immediately after commissioning so as not to jeopardize later secure operation. The access points may not be put into productive operation on delivery. For example, the name of the service set identifier (SSID) should not allow any conclusions about the hardware, the institution, any service providers and the purpose.

Those responsible must regularly check whether all security-relevant updates and patches for the established WLAN infrastructure have been recorded. So that the receiver and the transmitter interact optimally and safely, this must also be taken into account for the corresponding WLAN device drivers on the WLAN clients. A new software version or patch should only be installed after a reasonable test. The specified notification and information procedures in change management should describe who and how to inform about such changes. Likewise, the documentation of the WLAN infrastructure has to be adapted.

In the following it will be shown, with which recommendations the WLAN infrastructure can be further secured.

** Close all unused open ports **

Table 3: Close all unnecessary open ports

** Block unnecessary services **

For all three fictional scenarios, it is recommended to use the encryption method WPA2-AES-CCM (128 bit) instead of WPA2-TKIP.

The BSI Technical Guideline TR-02102 (see [TR02102]) contains recommendations for using SSL / TLS. These recommendations should be the basis for later activation of the used cipher suites. With which TLS version for which of the three fictive scenarios the information can be sufficiently secured, the following table shows.

Table 4: Recommended TLS versions per scenario

** Block unused management access **

In order to reduce potential attack vectors, the administration of the WLAN components z. For example, Secure Shell (SSH), HyperText Transfer Protocol Secure (HTTPS) or SNMP can be accessed from a dedicated management network. The WLAN infrastructure should not be administered via a WLAN-connected client.

To prevent intruder attacks, a central authentication based on personalized user accounts should be established. The authorizations stored for the user account of the administrator must follow the minimal principle.
In the context of emergency preparedness it is recommended to deposit a local user account (emergency user account). The password of the emergency user account must comply with the institution's established password policy. After each use of the emergency user account its password must be changed. Use and reason for action must subsequently be documented in a comprehensible manner.

** Detecting and blocking unauthorized user access **

ARP spoofing attacks should be detected and fended off when IP addresses are assigned via the DHCP server. For this purpose, DHCP snooping and dynamic ARP inspection (DAI) can be used.

#### NET.2.1.M6 Secure configuration of the WLAN clients

For secure WLAN operation, it is important that all clients coupled with the WLANs are also securely configured. Suitable requirements for secure configuration of clients are defined in the SYS 2.1 * General Client * and NET.2.2 * WLAN Usage * block. In addition, the WLAN interface must be deactivated if it is not used for a long period of time. The operation of WLANs must not be able to circumvent established security infrastructures (and in particular firewalls).

If WLAN clients (eg smartphones) are to provide hotspot-like functions themselves, users must ensure that they have changed preset SSIDs, cryptographic keys and passwords before activating the hotspot functions. The password (WPA2 key) should be chosen so that it is difficult to guess.

#### NET.2.1.M7 Structure of a Distribution System [Planner]

A distribution system connects the access points to each other and integrates the further infrastructure. There are two types of distribution systems:

* wired distribution systems (all access points are cabled among each other and with the further infrastructure)
* Wireless Distribution Systems (direct cabling between the access points is not necessary)
If high availability requirements are to be met, no wireless distribution system should be set up. In a wireless distribution system, repeaters must communicate with both the wireless clients and the access point. This reduces the transmission rate by half. This drastic reduction in the transmission rate can only be avoided by having clients and repeaters communicate with each other on a different frequency than repeaters and access points / wireless routers. Theoretically, a wireless distribution system with up to 254 repeaters can be operated in a network if the repeaters are not connected in series, but in the star, in order to avoid signal overlaps.

Before building a wired distribution system, decide whether to build a standalone physical switch infrastructure for the WLANs, a virtualized switch infrastructure or, alternatively, logical segmentation through Virtual Local Area Networks (VLANs). In particular, safety aspects must be taken into account.

#### NET.2.1.M8 Behavioral rules for WLAN security incidents

If the WLAN behaves in an unintended manner (eg WLAN is not available for a long time, access to network resources is not possible, network performance breaks down permanently), this may have been caused by a security incident. This may have been caused by an attacker, misconfiguration or system failure.

The IT operation should implement the following measures:

* Users must be able to reach IT operations through appropriate escalation levels.
* At the transfer point of the WLAN communication into the internal LAN, the communication should be selectively blocked per SSID, access point or even for the complete WLAN infrastructure in the event of an attack on the WLAN.
* In the event of a security incident or theft, IT operations should be able to take appropriate security measures. Ideally, they rely on coordinated and documented procedures. Possible actions are z. B .:

 
+ Shutdown of access points
+ Shutdown of servers
+ Check the configurations of the access points
+ Backing up all files that could provide information about the nature and cause of the problem that has occurred (for example, whether an attack actually occurred and how the attacker could invade it) d. H. in particular backup of all relevant log files.
+ If necessary, restore the original configuration data
+ Inform users to check their work areas for any irregularities.


 
If access points have been stolen, targeted security measures must be taken, such as: B .:

* Change all used cryptographic keys, so z. PSKs when using WPA2-PSK
* Configuration change on RADIUS servers to lock the stolen access point (IP, name, RADIUS client, shared secret, IPSec).
If WLAN clients have been stolen and a certificate-based authentication is used, the client certificates must also be blocked.

The possible consequences of safety-critical events must be investigated. Ultimately, all necessary measures must be taken to prevent the misuse of stolen devices to access the institution's network.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the area of ​​"WLAN operation".

#### NET.2.1.M9 Secure connection of WLANs to a LAN [planner]

The WLAN components must be secured at the transitions between WLANs and LAN, for example by a packet filter. In order to avoid unnecessary broadcast and multicast traffic, a corresponding VLAN should be established for each assigned SSID. Additional requirements that must be considered can be found in the module NET.1.1 * Network architecture and design *.

If WLANs are to be securely connected to a LAN, a distinction can be made between controller-based and controller-less administration of access points. Appropriate hedging measures for the respective variant are shown below.

** Controller-based management of access points **

For a controller-based management of the WLAN infrastructure, the following table provides appropriate safeguards for connecting the access point to the LAN.

Table 5: Recommended access point features per scenario

A pragmatic approach for local extraction of user data can be selected in part for Scenario 3, provided that the authorized access to the WLAN is checked by means of IEEE 802.1X and EAP-TLS and the access points and terminals fully support the IEEE 802.11ac standard. The communication between the access points and the WLAN controllers must also be cryptographically secured. To compensate for potential risks of losing the confidentiality and integrity of the information transmitted by radio, additional overlay encryption is recommended.

In Scenarios 1 and 2, user communication transitions directly from the access point to the internal networks via the switch. A pragmatic approach is therefore not possible. Only authorized access points of the institution incorporated into the established processes may be connected to the network. This should be ensured by means of IEEE 802.1X.
All access points receive their operating software directly from the assigned WLAN controller. The operating software of an access point is updated via a cryptographically secured channel. If the operating software is exchanged on the basis of clear-text protocols, the integrity of the software should then be verified by means of signatures.

The WLAN-typical communication ends for provisioned guest access must end in a demilitarized zone (DMZ). Access from the guest WLAN should be treated like access from the internet. They may only be admitted via a security gateway.

** Controller-less access point management **

A pragmatic approach is usually not possible with a controller-less management of the access points, since the user communication passes directly from the access point via the switch into the internal networks.

To provide roaming functions, autonomous networks are spanned between the individual access points, usually in the default VLAN. Whether the requirements for operating the access points are compatible with the security requirements can be checked with the following questions:

* Is the communication between the access points sufficiently cryptographically secured with each other?
* Is the group of employees with access to mirror ports at the switches known and limited?
* Is an unused switch port released from the default VLAN?
* Is a hardware authentication set up on the switch port?
* Are the roaming functions realized by bridging and tunneling methods?
* Does guest access communication end in a cryptographic tunnel in the DMZ?
Even for access points that are administered without a controller, only authorized access points of the institution that have been included in the established processes must be connected to the network. Use IEEE 802.1X to ensure that this requirement is met. The legitimate access of terminals to the WLAN should also be checked using IEEE 802.1X and EAP-TLS.

All access points receive their operating software directly from the assigned WLAN management system (WNMS). The operating software of an access point should be updated via a cryptographically secured channel. If the operating software is exchanged on the basis of clear-text protocols, the integrity of the software should then be verified by means of signatures.

The access points and integrated WLAN clients used should fully support the IEEE 802.11ac standard. The access point-to-access point communication must be based on Internet Protocol Security (IPsec) or TLS in an encapsulated tunnel.

#### NET.2.1.M10 Creation of a security policy for the operation of WLANs

An appropriate security policy should be established for the use of WLAN components in institutions. This WLAN-specific security policy should conform to the general security policy and the overall security policy of the institution. It should be regularly checked for up-to-dateness and adjusted if necessary.

A wireless security policy should include the following:

* It should describe who is allowed to install, configure and use WLAN components in the institution.
* Security measures and a default configuration should be specified for all WLAN components.
* If security issues are suspected, a security officer must be informed so that they can take further action (see also DER.2.1 Handling Incidents).
The IT operation should be informed about the hazards to which WLAN components are exposed and the security measures to be observed.

The correct implementation of the security measures described in the WLAN security policy should be checked regularly.
#### NET.2.1.M11 Suitable selection of WLAN components

Important criteria for selecting WLAN components are security, privacy and compatibility. Compatibility issues can not be ruled out with the large number of different WLAN components. To avoid compatibility issues, all components must be certified by the Wi-Fi Alliance and support the IEEE 802.11 standards. All WLAN components may only use frequency bands approved by the regulatory bodies of the country. Every provider of WLAN components must provide information on this in the data sheets for his product free of charge.

As part of the procurement of access points and corresponding management systems, the following should be checked:

* How many wireless channels can be managed?
Is the SSID adjustable?
* Which cryptographic methods are implemented?
* Can the desired modes be set for the authentication?
* Which EAP methods are supported?
* Can the administration be restricted to cryptographically secure communication channels? Can clear text protocols be switched off?
* Is Netflow version 9 (RFC 3954) usable for information flow control?
* Are access control mechanisms available?
* Are mechanisms integrated for an application-based implementation of Quality of Service?
Some wireless LAN components can be configured wirelessly directly over the WLAN. If this feature is an integral part of the components, it should be shut down to minimize risk. In order to implement established role and authorization concepts in the institution, administration access to WLAN components may only be possible for authorized persons.

As part of the procurement process, it should also be checked whether all WLAN components work correctly with the established network, security, authentication, monitoring and logging infrastructures. This includes z. For example:

* The authentication methods used in the WLAN must be supported by the operating systems and the hardware of the clients, the access points, the network management systems and the authentication servers.
* If the WLAN complies with IEEE 802.1X, the access points must support the authentication methods of the EAP family and correctly process the information communicated within IEEE 802.1X.
* In addition, it must be checked whether the authentication requests can be passed on to a central user database using secure query methods.
If it is planned to establish a larger WLAN infrastructure, it should be checked by means of an appropriate test, whether the defined and documented requirements are met before the infrastructure is finally procured.

#### NET.2.1.M12 Use of a suitable WLAN management solution

The scope of the WLAN management solution used should at least fulfill the following aspects:

* Documentation of the firmware versions of the access points and the WLAN clients,
* Documentation of configurations,
* History management of configuration changes,
* Evaluation and evaluation of alarms,
* Evaluation of troubleshooting statistics,
* Triggering of actions in case of a suspected security incident
* Adjustment of alarm trigger thresholds to a changed Wi-Fi usage,
* Logging and their meaningful preparation for the evaluation and
* Send log data to a central logging system for downstream evaluation.
In the case of WLAN configuration management, the central administration of security settings and the provision of secure installation and management channels are of crucial importance with regard to the security of an installation. From a security point of view, it is also strongly recommended that WLAN management systems help to monitor the air interface and interpret the measurement results and functions gained from it. These measurements and features include Rogue Access Point Detection, Wireless Intrusion Detection System (WIDS) and Wireless Intrusion Prevention System (WIPS). The two following tables name the minimum parameters for the detection of tampering and attacks for the three fictional scenarios.

Table 6: Detection of manipulations and attacks by a WIDS on the infrastructure

Table 7: Detection of tampering and attacks by a WIDS on the client

Policies can be managed centrally using a controller-based solution and WLAN traffic can be scheduled on the WLAN controller. As a result, z. B. the possibly existing guest traffic to the DMZ or firewall be forwarded. In a controller-less environment, the access points and downstream systems must take over this function via VPN.

Another aspect of the controller-based solution is that the failover and failback behaviors can be easily coordinated. The IT operation must ensure that network traffic is not impaired too much if an access point fails. In a controller-based model, the controller serves as a single point of coordination for all access points. If one of the access points fails, the controller reacts to keep latencies as short as possible. This is achieved by immediately forwarding the centrally stored session information of a WLAN user to an available access point. In controller-less infrastructures, this must be implemented by mechanisms similar to the routing protocol within the local network.

#### NET.2.1.M13 Regular security checks in WLANs

In order to be able to operate WLANs safely, it is particularly important to implement the security specifications and regularly check the availability. The measurements of the performance must be integrated into the existing monitoring and logging infrastructure. In the simplest case, a WLAN analysis can be carried out via a WLAN client, which is equipped with appropriate special software. However, this type of monitoring is only recommended for scenario 1. The WLAN infrastructure can be controlled better and more consistently if the necessary monitoring functions are integrated with the access points. With the help of integrated detectors in the access points, the following monitoring actions can be carried out automatically:

* Third-party devices (especially foreign access points) can be detected.
* Wireless Site Surveys can be conducted with the goal of obtaining coverage, data rates, transmission capacity, application bit rate, bit rate per user, quality of service (QoS), and more.
* The configuration of wireless network elements can be monitored.
IT operations should plan and commit the following tasks to ensure proper alarm and error handling:

* Alarms should be evaluated and evaluated.
* Statistics should be evaluated for troubleshooting.
* A suspected incident should trigger concerted action.
* If the WLAN usage has changed, the thresholds for triggering the alarm should be adjusted.
As part of a security check, a WLAN can also be examined for weak points by means of a penetration test. It must be checked carefully for all security measures taken to see if they are up to the attacks they are intended to counteract. Table 8 shows recommendations for time intervals to perform internal and external penetration tests.

Table 8: Recommended time intervals for regular penetration tests

#### NET.2.1.M14 Regular audits of the WLAN components

For all components of the WLAN infrastructure (access points, distribution system, WLAN management solution, etc.), it should be checked regularly whether all defined security measures have been implemented and correctly configured. Depending on the scope of functions provided, the WLAN management system should not only manage the current but also the previous configurations of the access points. Publicly established access points should be regularly randomly checked for violent opening or manipulation attempts. If any irregularities or weaknesses are detected, they should be documented. Deviations should be investigated.

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### NET.2.1.M15 Using a VPN to Secure WLANs (CI)

In order to additionally secure the communication over the WLAN infrastructure and thus to ensure that the transmission is fully secured in accordance with protection requirements, a VPN should be used. Further information on VPN can be found in the NET.3.3 * VPN * module or the associated implementation notes.

#### NET.2.1.M16 Additional security for the connection of WLANs to a LAN (CIA)

If a WLAN infrastructure is connected to a LAN, the transition between WLAN and LAN infrastructure should be protected in accordance with the higher protection requirements, for example by means of an intrusion detection system or intrusion prevention system (IDS / IPS). Additional information on IDS / IPS can be found in the NET.3.4 * IDS / IPS * module or in the associated implementation notes.

#### NET.2.1.M17 Securing Communication Between Access Points (C)

Between the access points, communication should be encrypted via the radio interface and the LAN in order to ensure the confidentiality of the transmitted information.

** Communication via the radio interface **

In order to secure the communication via the radio interface, the measures NET.2.1.M3 * Selection of suitable crypto procedures for WLAN * and NET.2.1.M5 * Secure basic configuration of the access points * are to be used.

** Communication between access point and WLAN management system **

Due to the increased protection requirements, it is assumed that the communication between an access point and the WLAN management system is not cloud-based. The following table lists protocols that can be used to secure the communication. The protection requirement to be met is taken into account.

Table 9: Communication between access point and WLAN management system

** Communication from Access Point to Access Point **

A communication from access point to access point is not directly possible in the controller-based WLAN infrastructure, but always takes place via the central WLAN controller. The possible protocols and associated authentication methods have already been shown in Table 9. The following table therefore only lists the protocols and associated authentication methods for a controller-less WLAN infrastructure.
Table 10: Communication from Access Point to Access Point

The indicated GRE protocol in Example 1 does not itself provide encryption and does not sufficiently protect the confidentiality and integrity for roaming and WLAN management information. It only serves to sensitize the selection of WLAN products and should not be used.

#### NET.2.1.M18 Using Wireless Intrusion Detection / Wireless Intrusion Prevention Systems (CIA)

WIDS / WIPS should be used to promptly identify security incidents and vulnerabilities and take appropriate countermeasures.

3 Further information
------------------------------

### 3.1 Worth knowing

WLANs can be operated in two different architectures. In ad hoc mode, two or more mobile devices (ie clients) equipped with WLAN functionality communicate directly with each other. In most cases, a WLAN will operate in infrastructure mode; H. Client communication takes place via central access points. The access points are also used to connect to wired LAN segments.

The infrastructure mode allows several deployment variants:

* By means of several access points, overlapping radio cells can be installed, so that the radio connection can be maintained when a client transfers to the next radio cell ("roaming"). Two access points can be used as a bridge between two wired LANs. Similarly, the use of an access point as a relay station (repeater) is possible to increase the range
* If appropriate components (directional antennas) are used at the access points, WLANs can also be used to network real estate. According to the manufacturer, ranges in the kilometer range can be achieved here. The access points can be operated as relay station or bridge.
The IEEE 802.11 standard uses the term Independent Basic Service Set (IBSS) for radio networks in ad-hoc mode and Basic Service Set (BSS) for constellations in infrastructure mode with an access point. Several coupled BSS are referred to as Extended Service Set (ESS), the coupling network is called Distribution System (DS).

In the 2.4 GHz frequency range, 13 frequency channels with a frequency spacing of 5 MHz are available for radio transmission in Germany. With a channel bandwidth of approx. 22 MHz, however, only a maximum of 3 channels can be used simultaneously without overlapping. In the frequency range from 5.15 to 5.35 GHz and at 5.47 to 5.725 GHz, a total of 19 channels have been released in Germany at a distance of 20 MHz, subject to conditions. With a channel bandwidth of 20 MHz directly adjacent channels are not disturbed here. Military and civilian radar and navigation applications also operate in the 5 GHz frequency range, and only systems that support dynamic frequency selection and transmission power adaptation should be used.

The mechanisms defined in IEEE 802.11 are used exclusively to secure the radio link between the clients and access points.

As an additional protection of the authentication, the Extensible Authentication Protocol (EAP) according to standard IEEE 802.1X can be used. EAP is described in detail in RFC 3748. Users log in to an authentication instance here, e.g. On a RADIUS server, and it checks the access authorization before the session key is exchanged. EAP supports a number of authentication methods so that certificates and two-factor authentication can also be used.

### 3.2 Literature

Additional information on hazards and security measures in the area of ​​"WLAN operation" can be found in the following publications, among others:

* #### [BSIDKS] Wireless communication systems and their security aspects
Federal Office for Information Security (BSI), 2009 <https://www.bsi.bund.de/DE/Publikationen/Broschueren/Drahtloskom/drahtloskom.html>

 
* #### [IEEE] Institute of Electrical and Electronics Engineers (IEEE)

  

 IEEE, (last accessed on 05.10.2017)
 <Https://www.ieee.org/index.html>

 
* #### [ISIWLAN] BSI Internet Security Standard (ISi Series)

  

 Secure connection of local networks to the Internet (Isi-LANA), Federal Office for Information Security (BSI), 2014
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/ standard criteria / ISi series / ISi-LANA / lana_node.html)

 
* #### [KB2977292] Microsoft security advisory

  

 Security Update for Windows 7 for x64-based Systems, (last accessed 05.10.2017)
 <Https://www.microsoft.com/de-de/download/details.aspx?id=44350>

 
* #### [NIST800153] NIST Special Publication 800-153

  

 Guidelines for Securing Wireless Local Area Networks (WLANs), NIST, 02-2012 http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-153.pdf

 
* #### [NIST80097] NIST Special Publication 800-97

  

 Establishing Wireless Robust Security Networks, A Guide to IEEE 802.11, NIST, 02.2007
 <Http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>

 
* #### [RSWLAN] More legal security for WLAN

  

 BMWi, (last accessed on 05.10.2017)
 <Https://www.bmwi.de/Redaktion/DE/Artikel/Digitale-Welt/wlan.html>

 
* #### [TR03103] Technical Guideline Secure Wireless LAN

  

 Federal Office for Information Security (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html]https://www.bsi.bund.de /DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
* #### [WIFIA] Wi-Fi Alliance

  

 The worldwide netword of companies, (last accessed 05.10.2017)
 <Http://www.wi-fi.org/>
