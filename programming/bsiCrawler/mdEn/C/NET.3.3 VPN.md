1 description
--------------

### 1.1 Introduction

Virtual Private Networks (VPNs) can be used to implement security measures to transfer sensitive data over non-trusted networks, such as the Internet. A VPN is a network that is physically operated within another network, such as the Internet, but is logically disconnected from that network. VPNs can use cryptographic techniques to protect the integrity and confidentiality of data. The secure authentication of the communication partners is also possible if several networks or computers are connected via leased lines or public networks.

### 1.2 Objective

The module defines requirements with which a VPN can be purposefully and safely planned, implemented and operated.

### 1.3 Delimitation

A VPN in terms of this building block is a network that is physically operated within another network, but is logically disconnected from that network. The VPN building block does not address the basics for secure networks (see NET.1.1 * Network architecture and design *). Nor does it cover all processes related to the operation of a VPN. In particular, the building blocks OPS.1.1.3 * Patch and Change Management *, ORP.3 * Information Security and Training *, CON.1 * Crypto Concept *, OPS.1.1.5 * Data Backup *, DER.4 * Emergency Management * and OPS.2.4 * Remote Maintenance * g.

The module must be used for every type of remote access to the information network. These include connections via data networks, such as site-to-site, end-to-end or remote access VPNs, and via telecommunications links, such as analog dial-up, ISDN or cellular phones. This module only covers VPN systems for layers 2 (data link layer) to 4 (transport layer) of the Open Systems Interconnection (OSI) model.

Recommendations on how to configure the operating systems of the VPN endpoints are also not part of this module. Corresponding requirements can be found in the block SYS.1.1 * General Server * or SYS.2.1 * General Client * as well as the respective operating system-specific blocks of the IT-Grundschutz Compendium.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​VPN:

### 2 1 Lack of or inadequate planning and regulation of VPN deployment

If the VPN is not carefully planned, set up, or configured, security vulnerabilities may occur that affect all IT systems networked to the VPN. Attackers may thus be able to access confidential information of the institution.

For example, with inadequate VPN scheduling and regimentation, it is possible that users were not properly trained, thereby using the VPN in an insecure environment or dialing in from an insecure client. This may allow attackers to access the entire corporate network.

Even if the regular monitoring of access to the VPN was inadequately planned, attacks could not be detected in time. Thus, it is not possible to react promptly and an attacker can steal data unnoticed or sabotage entire processes.

### 2 2 Insecure VPN service providers

VPN connections can reach into critical areas of the network. If the institution uses a VPN service provider and has not chosen it carefully, this could make the entire network of the institution unsafe. For example, an insecure VPN service offered by attackers could be used by attackers to steal targeted information.

### 2 3 Problems with local storage of authentication data for VPNs
Many VPN clients for remote access allow the data required for authentication to be saved locally so that the user does not have to enter them again when reconnecting. If an attacker succeeds in gaining access to the VPN client, he may be able to read the credentials and log in to the network as a legitimate user. Thus, he can access the local networks and the information and services of the institution that can be accessed therein.

### 2 4 Insecure configuration of VPN clients for remote access

If a VPN client is not configured securely, users could use their security mechanisms incorrectly or not at all. Also, they may change the configuration of the client. It is also possible by an insecure configuration that software installed by the user also endangers the security of the VPN client.

### 2 5 Insecure default settings on VPN components

The default settings of VPN components do not always have all the features of a secure installation. Often more attention is paid to usability and ease of integration with existing systems than security. If VPN components are not or only insufficiently adapted to the specific security needs of the institution, weak points and thus dangerous points of attack can arise. For example, the entire VPN and thus the internal network of the institution is vulnerable if the manufacturer does not change the default passwords.

### 2 6 Theft of mobile devices with VPN client

Mobile devices are often stolen or otherwise lost. As a result, the danger exists that attackers can access the institution's internal network via the VPN connection established there. Often missing loss reporting processes, so z. For example, if a stolen laptop is not promptly reported to the correct location in the institution. As a result, the attacker may have long been unnoticed in the internal network and copy numerous information worthy of protection.

3 requirements
---------------

The following are specific requirements for the VPN area. Basically, the IT operation is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.3.3.A1 Planning the VPN deployment

Before the introduction of a VPN, careful planning MUST be done. The responsibilities for the VPN operation MUST be defined. It also MUST be scheduled for the VPN user groups and their permissions. It also MUST be defined how documented, changed or revoked access permissions are to be documented.

#### NET.3.3.A2 Selection of a VPN Service Provider [Information Security Officer (ISB)]

With a VPN service provider, Service Level Agreements (SLAs) MUST be negotiated and documented in writing. It MUST be regularly checked if the VPN service provider complies with the agreed SLAs.

#### NET.3.3.A3 Secure installation of VPN terminals
The underlying operating system of the VPN platform MUST be securely configured. If an appliance is used, there must be a valid maintenance contract. It MUST be ensured that only qualified personnel install VPN components. The installation of the VPN components as well as possible deviations from the planning specifications SHOULD be documented. The functionality and the chosen security mechanisms of the VPN MUST be checked before commissioning.

#### NET.3.3.A4 Secure configuration of a VPN

For VPN clients, VPN servers and VPN connections, a secure configuration MUST be set. This SHOULD be suitably documented. Also, the responsible administrator MUST check regularly whether the configuration is still secure and possibly adapt it for all IT systems.

#### NET.3.3.A5 Blocking of unneeded VPN accesses

It must be regularly checked if only authorized IT systems and users can access the VPN. No longer required VPN access MUST be deactivated in a timely manner. VPN access MUST be limited to the required usage times.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of VPN. They SHOULD be implemented in principle.

#### NET.3.3.A6 Perform a VPN requirement analysis

A requirements analysis SHOULD be carried out in order to be able to determine the application scenarios for the respective VPN and derive therefrom requirements for the required hardware and software components. In the requirements analysis the following points SHOULD be considered:

* Business processes,
* Access paths,
* Identification and authentication procedures,
* Users and user permissions,
* Responsibilities and
* Reporting channels.
#### NET.3.3.A7 Planning of technical VPN realization

In addition to the general planning (see NET.3.3.A1 * Planning the VPN deployment *), the technical aspects of a VPN should be carefully planned. For example, VPN encryption procedures, VPN endpoints, allowed access protocols, services and resources should be specified. In addition, the subnets (see NET.1.1 * Network Architecture and Design *) that can be reached via the VPN SHOULD be defined.

#### NET.3.3.A8 Create a security policy for VPN use

A security policy for VPN usage SHOULD be created and communicated to employees. The security measures SHOULD be explained during training sessions. If a VPN access is set up for an employee, SHOULD he be given a leaflet containing the most important VPN security mechanisms. All VPN users SHOULD be required to comply with security policies.

#### NET.3.3.A9 Appropriate selection of VPN products

When selecting VPN products, the requirements of the institutions for the networking of different locations and the connection of mobile employees or teleworkers SHOULD be taken into account.

#### NET.3.3.A10 Secure operation of a VPN

For VPNs, an operating concept SHOULD be created. This should include the aspects quality management, monitoring, maintenance, training and authorization.

#### NET.3.3.A11 Secure connection of an external network

If a VPN is used to connect to an external network, then in the current state of the art, safer authentication and encryption methods with a sufficient key length SHOULD be used. Also the chosen method of key exchange SHOULD comply with the state of the art. It should be ensured that VPN connections are established only between the IT systems and services provided for this purpose. The tunnel protocols used in this case SHOULD be suitable for use.

#### NET.3.3.A12 User and Access Management for Remote Access VPNs
For remote access VPNs, a centralized and consistent user and access management SHOULD be ensured. The authentication methods used SHOULD meet the requirements of the ORP.4 * identity and authorization management module *.

When using stand-alone servers for user and access management, MAKE SURE they are set up and operated securely and consistently to the requirements of the ORP.4 * Identity and Permissions Management * building block. Furthermore, the servers used SHOULD be protected against unauthorized access.

#### NET.3.3.A13 Integration of VPN components in a firewall

The VPN components SHOULD be integrated into the firewall so that traffic can be effectively controlled and filtered. It SHOULD document how the VPN components are integrated into the firewall.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the "VPN" area can be found in the following publications, among others:

* #### [27033-5] ISO / IEC 27033-5: 2013

  

 Information technology - Security techniques - Network Security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs), ISO, 08.2013
 <Https://www.iso.org/standard/51584.html>

 
* #### [ISIVPN] Virtual Private Network (ISi-VPN)

  

 BSI Guideline on Internet Security (ISi-L), BSI, 2009
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi\_vpn\_leitlinie\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/ DE / BSI / Internet security / isi_vpn_leitlinie_pdf.pdf)

 
* #### [NIST80077] NIST Special Publication 800-77

  

 Guide to IPsec VPNs, NIST, 12.2005
 <Http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-77.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "VPN" block.

* G 0.9 Failure or malfunction of communication networks
* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.28 Software vulnerabilities or errors
* G 0.32 Abuse of permissions
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.
  * NET.3.3.A3 Secure installation of VPN terminals
  * NET.3.3.A9 Appropriate selection of VPN products
  * NET.3.3.A11 Secure connection of an external network
* G 0.11 Failure or disruption of service providers
  * NET.3.3.A2 Selection of a VPN Service Provider [Information Security Officer (ISB)]
  * NET.3.3.A9 Appropriate selection of VPN products
  * NET.3.3.A11 Secure connection of an external network
* G 0.14 Spying out information (spying)
  * NET.3.3.A4 Secure configuration of a VPN
  * NET.3.3.A7 Planning of technical VPN realization
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A13 Integration of VPN components in a firewall
* G 0.18 Missing planning or missing adjustment
  * NET.3.3.A1 Planning the VPN deployment
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A11 Secure connection of an external network
  * NET.3.3.A12 User and Access Management for Remote Access VPNs
  * NET.3.3.A13 Integration of VPN components in a firewall
  * NET.3.3.A3 Secure installation of VPN terminals
  * NET.3.3.A6 Perform a VPN requirement analysis
  * NET.3.3.A8 Create a security policy for VPN use
* G 0.19 Disclosure of information worthy of protection
  * NET.3.3.A4 Secure configuration of a VPN
  * NET.3.3.A7 Planning of technical VPN realization
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A13 Integration of VPN components in a firewall
* G 0.22 Manipulation of information
  * NET.3.3.A4 Secure configuration of a VPN
  * NET.3.3.A7 Planning of technical VPN realization
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A13 Integration of VPN components in a firewall
* G 0.23 Unauthorized intrusion into IT systems
  * NET.3.3.A4 Secure configuration of a VPN
  * NET.3.3.A6 Perform a VPN requirement analysis
  * NET.3.3.A7 Planning of technical VPN realization
* G 0.28 Software vulnerabilities or errors
  * NET.3.3.A5 Blocking of unneeded VPN accesses
* G 0.32 Abuse of permissions
  * NET.3.3.A1 Planning the VPN deployment
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A11 Secure connection of an external network
  * NET.3.3.A12 User and Access Management for Remote Access VPNs
  * NET.3.3.A13 Integration of VPN components in a firewall
  * NET.3.3.A4 Secure configuration of a VPN
  * NET.3.3.A6 Perform a VPN requirement analysis
  * NET.3.3.A12 User and Access Management for Remote Access VPNs
* G 0.40 Denial of Service
  * NET.3.3.A9 Appropriate selection of VPN products
  * NET.3.3.A11 Secure connection of an external network
* G 0.43 Importing messages
  * NET.3.3.A7 Planning of technical VPN realization
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A13 Integration of VPN components in a firewall
* G 0.46 Loss of integrity of sensitive information
  * NET.3.3.A7 Planning of technical VPN realization
  * NET.3.3.A10 Secure operation of a VPN
  * NET.3.3.A13 Integration of VPN components in a firewall
