1 description
--------------

### 1.1 Introduction

Wireless LANs (WLANs) can be used to set up wireless local area networks or extend existing wired networks. To date, almost all WLAN components available on the market are based on the IEEE 802.11 standard and its additions. A special role is played by the manufacturer consortium Wi-Fi Alliance, which has created an industry standard based on the IEEE 802.11 standard with "Wi-Fi". The Wi-Fi Alliance confirms with the Wi-Fi seal of approval that a device has passed certain interoperability and conformance tests.

All users (including management of the institution) must be informed about WLAN basics and sensitized to possible dangers that may arise if WLANs are used improperly. They must have the necessary knowledge to properly understand and apply safety measures. In particular, they must be aware of what is expected of them in terms of information security and how they should react in certain situations when using WLANs.

### 1.2 Life cycle

** planning and conception **

Before WLANs are operated and used, a careful planning is necessary. In order not to overload users with too much operational and security-related details of a WLAN infrastructure, a separate WLAN policy should be created specifically for this target group (see NET.2.2.M1 * Creation of a user policy for WLAN *).

**Implementation**

In order to meet the security requirements of the institution in the daily use of WLANs, the users must be involved. So they have to be informed about security measures that can not only be implemented by technical means and that require their participation. In order to minimize security incidents and to point out potential dangers that may arise when WLANs are used improperly, users should be sufficiently trained and sensitized (see NET.2.2.M2 * Sensitization and training of WLAN users *).

**Business **

If external hotspots are to be used, employees must be specifically trained in the use of hotspots and implement appropriate measures (see NET.2.2.M3 * Securing WLAN Usage in Unsafe Environments *).

** Emergency Preparedness **

If attacks on a WLAN or within a WLAN have been detected, the users of the WLAN must know how to behave (see NET.2.2.M4 * Behavior rules for WLAN security incidents *).

2 measures
-----------

The following are specific implementation tips in the "Wi-Fi Usage" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### NET.2.2.M1 Creation of a user policy for WLAN [Head IT]

In order not to overload users with too much operational and security-related details of a WLAN infrastructure, a separate WLAN policy should be created especially for this target group. The user policy builds on the institution's overall security policy and pinpoints the key aspects of how to use WLANs safely. In such a user policy then briefly the specifics of the Wi-Fi use should be described, such. B.

* with which internal and external networks the WLAN clients may be connected,
* Under what conditions you are allowed to log in to internal or external WLANs,
* if and how hotspots may be used,
* that the ad-hoc mode must be switched off so that no other client can access the WLAN clients directly,
* What steps should be taken in case of (suspected) compromise of the WLAN clients, especially who to notify.
It is also important to clearly describe how to deal with client-side security solutions. This includes, for example, that

* no security-relevant configurations may be changed,* an existing personal firewall must not be switched off,
* disabled all shares of directories or services, or at least protected by good passwords,
* For the use of external WLANs, if possible only special user accounts with restrictive rights assignment should be used.
In addition, the user policy should include a clear ban on unauthorized access points to the institution's LAN. It must also be pointed out in the guideline that the WLAN interface must be deactivated if it is not used for a longer period of time. Furthermore, the Directive should specify, in particular as regards the use of classified information, such as classified information, which data may be used and transmitted in WLANs and which may not. Users should be made aware of Wi-Fi threats as well as the content and implications of the Wi-Fi policy.

It is necessary to check regularly whether the contents required by the directive have been correctly implemented and the results should be well documented.

#### NET.2.2.M2 Sensitization and training of WLAN users [Supervisors, Head of IT]

Today almost every employee is equipped with a mobile device and can connect to a public or internal WLAN. Mobile devices (eg smartphones) can be used to create WLAN hotspots for others or to set up ad hoc WLANs. These versatile uses can create security issues if the devices are used improperly. Therefore, all employees must be sensitized accordingly. This can be done, for example, by means of a leaflet on possible dangers associated with the use of WLANs. The leaflet should also contain the most important measures and behaviors in order to counteract the corresponding hazards. The leaflet should be handed over together with the devices so that the users can handle the devices responsibly and conscientiously use them. Should users be allowed to provide themselves or others with a WLAN (as a hotspot) via their device, the training content should also contain the associated hazards and measures. For example, it may be pointed out that WLAN communication can be protected by configuring a complex password.

Sensitization, especially of users who are allowed to access confidential information, should be practiced and supported by means of practical examples.

A special hazard for the WLAN clients exists when public radio networks (so-called hotspots) are used. Hotspots often use no or only weak security mechanisms to give customers straightforward access. As a result, transmitted information can usually be easily intercepted. If hotspots are to be used for the dial-in to the institution or if confidential information is to be transmitted to them, users must be specifically trained in the use of hotspots and implement appropriate measures. For example, they must make sure that all connections are properly encrypted. Any suspicion of alerts or redirects to IT systems that are not part of the institution must be considered to be a security incident.

It must be clear to users that using WLANs greatly enhances mobility, but it also carries risks as attackers may be out of the field of view or suspected spatial WLAN coverage.

#### NET.2.2.M3 Securing WLAN Usage in Unsafe Environments [IT Operations]Hotspots are a limited radio area. Most hotspots are explicitly built so that they can be used by foreign participants. Their main purpose is usually wireless access to the Internet. Often you can find such hotspots in hotels, airports, exhibition halls, railway stations and convention centers.

Hotspots should always be regarded as an insecure network, firstly because the level of security available there is difficult to assess from the outside, and secondly because most hotspots offer their services in the form of "shared networks". As a result, it is generally possible to access every other terminal in the network from each terminal. If the risk arising from the use of a hotspot can not be estimated, it may be considered that the use of hotspots should be completely prohibited by the WLAN security guideline.

The operators of hotspots can do a lot for the security of the radio link and other services offered by them (see NET.2.3 * Operation of Hotspots *), but without the cooperation of the users a reasonable security can not be achieved. These include the following measures:

* Every user of a hotspot should know his or her security requirements and decide whether or under which conditions he is allowed to use the hotspot.
* Registration at the hotspot is usually via a web portal or via a web application. This must ensure the protection of the registration information. Authentication should always be encrypted.
* WLANs that were only sporadically used should be removed by the users from the history. For this purpose, the identifier of the WLAN (SSID) is removed from the list. This prevents the device from unintentionally logging into the WLAN.
* If possible, special user accounts with secure basic configuration and restrictive rights should be created for the use of hotspots. Under no circumstances should a user with administrator rights log on to external WLANs from his client.
* At the latest when financial, personal or other sensitive data such as credit card numbers, PINs, passwords or emails are to be transmitted, it must be ensured that all necessary security measures on the clients, especially encryption, are activated. An example of this would be the secure processing of e-mails via an HTTPS web interface. Confidential information may never be transmitted unencrypted over foreign networks.
* Users are only allowed to access internal resources of the institution via VPNs via third-party WLANs (eg provided guest access by third-party institutions or public hotspots). As a result, communication to one's own institution can be additionally secured independently of the established protection mechanisms of the WLAN infrastructure used. Further information can be found in the NET.3.3 VPN block or in the associated implementation notes.
### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the area of ​​"WLAN use".

#### NET.2.2.M4 Behavioral rules for WLAN security incidents

If the WLAN behaves in an unintended manner (eg WLAN is not available for a long time, network resources can not be accessed, network performance breaks down permanently), this may have been caused by a security incident.

The Wi-Fi users should do the following:

* You should back up your work, stop Wi-Fi access, and disable your client's Wi-Fi interface.* If error messages appear or the client did not behave normally, they should be documented by the user. It should also be documented what the user did before or during the security incident. With this information, IT operations may be able to more quickly pinpoint the cause and impact of the incident and more effectively initiate countermeasures.
* In addition, they should notify the IT operation via an appropriate escalation level.
### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

3 Further information
------------------------------

### 3.1 Worth knowing

Beyond the module, the implementation notes and the literature review, there is currently no further information worth knowing.

### 3.2 Literature

Additional information on hazards and security measures in the area of ​​"WLAN use" can be found in the following publications, among others:

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

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

 
* #### [TR03103] Technical Guideline Secure Wireless LAN

  

 Federal Office for Information Security (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html]https://www.bsi.bund.de /DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
* #### [WIFIA] Wi-Fi Alliance

  

 The worldwide netword of companies, (last accessed 05.10.2017)
 <Http://www.wi-fi.org/>