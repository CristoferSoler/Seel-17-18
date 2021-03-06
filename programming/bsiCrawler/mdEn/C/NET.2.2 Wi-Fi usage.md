1 description
--------------

### 1.1 Introduction

Wireless LANs (WLANs) can be used to set up wireless local area networks or extend existing wired networks. To date, almost all WLAN components available on the market are based on the IEEE 802.11 standard and its additions. A special role is played by the manufacturer consortium Wi-Fi Alliance, which has created an industry standard based on the IEEE 802.11 standard with "Wi-Fi". The Wi-Fi Alliance confirms with the Wi-Fi seal of approval that a device has passed certain interoperability and conformance tests.

WLANs offer a gain in convenience and mobility, but use also poses additional potential for security of information security by communicating wirelessly. It is therefore essential that, in addition to the IT managers, the users are also sensitized to the potential dangers that can arise if WLANs are used improperly. This means that users must have the necessary knowledge to properly understand and apply security measures. In particular, they must be aware of what is expected of them in terms of information security and how they should respond in certain situations when using WLANs.

### 1.2 Objective

In this module will be shown how WLANs can be used safely.

### 1.3 Delimitation

The module contains basic requirements that must be observed and fulfilled when using WLANs in order to be able to counteract the specific hazards. Requirements that can be used to operate WLANs safely, however, are not the subject of this module, but are described in the module NET.2.1 * WLAN operation *. In addition, the building block does not address general aspects of a client. Such aspects are discussed in the SYS2.1 * Common Client * building block.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​WLAN usage:

### 2 1 Insufficient knowledge of regulations

If the users are not sufficiently familiar with the rules for the correct handling of WLANs, they can not comply with it. If, for example, WLAN clients are thoughtlessly connected to foreign networks, the information transmitted via them (eg session cookies, passwords) can be intercepted.

### 2 2 Non-compliance with safety measures

Due to negligence and lack of controls, it happens again and again that people do not take into account the recommended or ordered security measures or not to the full extent. If, for example, a WLAN client is used in ad hoc mode, although this is expressly forbidden in the user policy, another client can communicate directly with the WLAN client. B. unauthorized access to confidential documents stored on the client.

### 2 3 Listening to the WLAN communication

Since radio is a medium that several users can share ("shared medium"), the data transmitted via WLANs can be easily monitored and recorded. If the data is not or insufficiently encrypted, transmitted payload data can be easily obtained. In addition, radio networks or the radio waves transmitted often exceed the limits of the self-occupied premises, so that data are also broadcast in areas that can not be controlled and secured by the users or an institution.

### 2 4 Evaluation of connection data in wireless communication

For WLANs based on IEEE 802.11, the MAC address of a WLAN card is sent with every data transfer. Since it is transmitted unencrypted, motion profiles can be created via mobile users, eg. For example, when they log into public hotspots.### 2 5 Imitation of a valid access point (rogue access point)

An attacker can pretend to be part of the WLAN infrastructure by installing their own access point with a properly chosen SSID near a client. This fake access point is called a rogue access point. If this provides the WLAN client with a higher transmission power than the real access point, the client will use it as the base station if two-sided authentication is not enforced. In addition, the real access point could be turned off by a denial-of-service attack. Users log on to a network that only pretends to be the destination network. This makes it possible for an attacker to listen to the communication. Poisoning or spoofing methods also allow an attacker to fake a false identity or to redirect network traffic to his systems. So he can eavesdrop and control the communication. Especially in public radio networks (so-called hotspots) a rogue access point is a popular means of attack.

3 requirements
---------------

The following are specific requirements for Wi-Fi usage. Basically, the user is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.2.2.A1 Creation of a user policy for WLAN [Head IT]

On the basis of the institution's general security policy, the essential core aspects for secure WLAN use MUST be specified in a WLAN user policy. Such a user policy MUST describe the specifics of WLAN usage, eg. For example, if and how hotspots may be used.

Furthermore, the Directive MUST, in particular with regard to the use of classified information, contain information about which data may be used and transmitted in the WLAN and which may not.

It MUST be described how to deal with client-side security solutions. The user policy MUST include a clear ban on connecting unauthorized access points to the institution's LAN. It also MUST be noted in the policy that the WLAN interface MUST be disabled if it is not used for an extended period of time.

It MUST be checked on a regular basis to see if the content required by the Directive has been properly implemented. The results SHOULD be sensibly documented.

#### NET.2.2.A2 Sensitization and training of WLAN users [Supervisors, Head of IT]

The users of WLAN components, especially of WLAN clients, MUST be sensitized and trained on the measures listed in the user policy. Users MUST be clear about what the WLAN-specific security settings mean and why they are important. In addition, you MUST be alerted to the dangers of bypassing or disabling these security settings.

The training contents MUST always be adapted according to the respective application scenarios. However, in addition to training on WLAN security mechanisms, users MUST also be presented with the wireless security policy of their institution. Likewise, they MUST be made aware of the dangers of using foreign WLANs.

#### NET.2.2.A3 Securing WLAN Usage in Unsafe Environments [IT Operations]MUST use external hotspots MUST be implemented:

* Any user of a hotspot MUST know his or her security requirements (see NET.2.2.A2 Wi-Fi Users' Awareness and Training) and then decide if and under which conditions he will be allowed to use the hotspot.
* WLANs that are only used sporadically SHOULD be deleted by the users from the history.
* If possible, separate user accounts with a secure base configuration and restrictive permissions SHOULD be used.
* It should be ensured that no user with administrator rights can log on to external WLANs from his client.
* Sensitive data MUST be transmitted ONLY if appropriate security measures are implemented and secure protocols are used.
* Publicly accessible WLANs MAY ONLY allow users to access the institution's internal resources via a Virtual Private Network (VPN). Further information can be found in the NET.3.3 VPN block.
### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​WLAN usage. They SHOULD be implemented in principle.

#### NET.2.2.A4 Behavioral rules for WLAN security incidents

For WLAN security incidents, users SHOULD implement the following:

* You SHOULD secure your work, stop your wireless access, and disable your client's Wi-Fi interface.
* Error messages and abnormalities SHOULD be accurately documented by the user. Likewise, users SHOULD document what they did before or while the security incident occurred.
* Users SHOULD notify IT operations through a suitable escalation level (eg User Help Desk).
### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

4 Further Information
------------------------------

### 4.1 Literature

Additional information on hazards and security measures in the area of ​​"WLAN use" can be found in the following publications, among others:

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

 
5 Appendix: Cross reference table for elementary hazards-------------------------------------------------- --------

The following elementary threats are important for the "WLAN usage" building block.

* G 0.15 Listening
* G 0.18 Missing planning or missing adjustment
* G 0.23 Unauthorized intrusion into IT systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.43 Importing messages
The cross reference tables can be found in the download area due to their size.