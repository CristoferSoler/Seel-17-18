1 description
--------------

### 1.1 Introduction

Smartphones and tablets are nowadays constant companions in the information society. They are constantly online, that is, connected to the Internet or the internal resources of an institution, thereby providing access to digital information at all times. Due to modern, simple operating concepts as well as high efficiency, smartphones and tablets from Apple are widely used in the professional environment. In order to reconcile the usability and flexibility requirements with the fulfillment of the security strategy and concepts of the institution, devices to be managed must be integrated into a mobile device management infrastructure. A reasonable exception, considering economic considerations, may be the management of a smaller, single-digit number of devices without the use of an MDM. Thus, almost all examples shown below can also be implemented with Apple's "Apple Configurator" for smaller device numbers. When using the Apple Configurator, security management should provide alternative response and information channels for a timely response to security incidents.

The following three fictitious user groups are used within this document to illustrate the different implementation recommendations, depending on the purpose of the device, the user group and access to information from the institution.

User group 1

* Users use the provided smartphones primarily for telephony and sending e-mails.
* Users have no further access to internal collaboration and document management systems.
* The information is not classified as confidential.
User group 2

* Users use the provided smartphones and tablets for telephony, e-mailing, and editing business documents.
* Users also have access to internal collaboration and document management systems.
* Sometimes the information is classified as sensitive or critical to business.
User group 3

* Users use the provided smartphones and tablets for telephony, e-mailing, and editing business documents.
* Users also have access to internal collaboration and document management systems, financial data or critical systems of the institution.
* Sometimes the information is classified as confidential.
### 1.2 Life cycle

 ** planning and conception **

In the planning and design phase, all possible usage scenarios, eg. For example, integration into a collaboration solution, access to merchandise management systems and the maximum protection requirements to be implemented, can be incorporated into the selection of the central management solution. If a strict separation between private and business areas is desired, it is advisable to check whether a separation of business and private information can be achieved by means of managed apps and managed open-in. Container solutions should also be considered. Similarly, at this stage, the review of the requirements for user-based integration of smartphones and tablets in the infrastructure should take place. According to the result of the check, requirements for the previous security gateways and their functions can, for. These include, for example, the automatic activation of filter rules for the user and their devices or the automatic withdrawal of access rights when active security policies are violated.
In the planning phase, the compatibility of the general terms and conditions of the Apple company with the business, security and data protection regulations of the institution to review. One thing to consider in any case is the verification of iCloud usage. Currently z. For example, the use of the iCloud account is intended for private use only. An overview of relevant terms and conditions is listed in chapter 3.2 Literature.

 **Procurement**

When purchasing smartphones and tablets as well as in the selection of the mobile service provider, the safety aspects should be considered in addition to the economic aspects. Examples: Is an institution-specific access point name (APN) required by the mobile service provider for simplified basic filtering of the allowed IP addresses of the devices? Should the authentication at the VPN gateway or the institutional WLAN be based on EAP-SIM? Does using the Device Registration Program (DEP) represent a more flexible alternative?

 **Implementation**

There are a variety of security mechanisms and approaches to the implementation to achieve the desired level of protection for smartphones and tablets. In Chapter 3 recommendations for the protection of smartphones and tablets based on the three initially defined user groups are shown. When implementing the implementation recommendations, so-called configuration profiles are rolled out on the managed devices. The roll-out can be done using Apple Push or EAS. Regardless of how the configuration profiles are rolled out to the managed devices, it must be ensured that users are unable to delete the configuration profiles without authorization.

 **Business**

For smartphones and tablets to be organized and used reliably, technical and organizational measures must be implemented. Some of the measures can not be rolled out centrally and consistently across all devices and require the assistance of the user. If the same hardening action is implemented by the person responsible in more than one configuration profile on the device, summing all the configuration profiles will apply the stricter setting on the target device.

Apple may provide regulatory access to Personal User Information from 16 data groups of the respective iCloud user account, subject to court orders. The 16 groups are described in detail in the document "Legal Process Guidelines" (see chapter 3.2). So the law enforcement agencies z. For example, they may receive information about the device's current geo-data, view Apple Store purchases and transactions, iCloud content, such as documents, activation information, registration data, and game center links.

 ** ** segregation

Traditionally, overwriting the data safely is recommended for secure disk wiping. With flash memory, as it is installed in iOS-based smartphones and tablets, the internal memory blocks can not be addressed directly by design. This means that the functions for resetting the operating system must be used to clear the data. Resetting to factory settings is a sufficient method of erasing information with normal protection requirements. If information with high protection requirements has been processed or stored on the device, destruction of the device according to DIN 66399 is the safe method.

 ** Emergency Preparedness **

In the course of emergency preparedness agreements should be made with contractors regarding the MDM and the provision of a sufficient number of terminals. It should also be planned how to deal with the loss of terminals or the data stored on them.

2 measures
-----------
The following are specific implementation notes in the iOS (for Enterprise) section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.3.2.3.M1 iOS usage strategy

Basically, all MDM providers rely on the interfaces released by the Apple company and usually support a short time after releasing a new version of iOS newly added functions. This means that the MDM must support at least the required safeguards and be integrated into the existing infrastructure. Operation of the MDM and the managed devices must not cause loss of confidentiality, integrity, and availability of the information and associated systems. It has to be considered whether the MDM should be operated in the cloud, on-site in one's own data centers or at a data center service provider certified to BSI IT-Grundschutz.

For easier initial startup, the option of device enrollment via the Apple DEP can be used. In-depth information will be provided via the web link provided in chapter 3.2.

When using iOS devices, it is first necessary to clarify certain strategic issues that might be relevant to their use, such as: Depending on your own IT infrastructure. As far as possible, data should not be stored exclusively on the mobile devices so that they are not lost in case of loss. This also affects the overall backup strategy of the institution.

Depending on the intended purpose, a suitable terminal selection must be made. It is also important to clarify at an early stage whether third-party apps should be used on the iOS devices.

#### SYS.3.2.3.M2 Planning the use of cloud services

When using online storage services (eg Microsoft Cloud, Google Drive, Dropbox, iCloud) a distinction can be made between different variants. The online backup, in which data is stored once or at regular intervals over the Internet in order to be retrieved after a loss of data, represents the simplest form of use. In the so-called online hard drive depending on the service provider Pure data storage also provides additional functions such as sharing data with employees, friends or business partners, collaborating on documents, and syncing various devices.

If access to the data of the institution is not possible because the online storage service is not available due to a failure of the service provider or the connection to the service, this can disrupt or completely disrupt the business processes. In this context, the protection requirements for the information concerned are particularly important. Insofar as high availability is the basis of the processes, financial losses usually result in prolonged downtimes of the online service, usually accompanied by image damage. In addition to the availability of online storage and the information stored in it, especially the confidentiality of information has a high priority. If attackers succeed in gaining access to confidential information of the institution and B. make it accessible to a wider group of people threatened image loss as well as legal consequences and financial losses.

When transferring information, processing it over the network or storing it, integrity problems can occur that can even lead to total loss. This also applies to encrypted data. The implications for the institution are similar to the loss of confidentiality.
Legal aspects in the use of cloud services always play a role when personal data in the sense of §3 paragraph 1 Federal Data Protection Act (BDSG) are handed over. Such order data processing, depending on the actual location of the data, according to §11 BDSG only under certain conditions possible and also bound to the issue of a written order. In the event of an infringement, institutions run the risk of violating existing law and thereby not only damage their reputation, but also face damage claims or fines.

If at the end of the contract the information of the institution is not deleted by the provider of the online storage, there is a risk that unauthorized persons will continue to gain access to this information.

Further information on these topics can be found in the corresponding modules.

iOS-based devices basically provide a close link with the iCloud services of the manufacturer Apple. Via the App Store, additional apps can be installed on the device to simplify the integration of additional cloud service providers. In the run-up to the use of smartphones and tablets, those responsible for provider management, operation and procurement must be given the required operational, security and data protection requirements in accordance with internal guidelines.

#### SYS.3.2.3.M3 Using the device code

By activating the passcode unauthorized third parties should be denied access to the information in the smartphone or tablet. For the three fictitious user groups, the following configurations listed in the table are recommended for basic access security based on the purpose and protection needs of the information.

Table: Using the device code (passcode)

#### SYS.3.2.3.M4 Using the Automatic Lock Configuration Option

The configuration option "automatic lock" is the same as the screen lock on a PC. This means that when not in use, an internal counter is started and the screen is locked after reaching the specified time. By a low value can thus be ensured that an unused or short-term unattended device can not be used by an unauthorized without authentication. When determining the time span, the values ​​for a stationary PC should not be taken as the basis, but rather the intended purpose, the place of use, the determined protection requirements, the usability requirements and the agreed complexity of the passcode. For the three fictitious user groups, the time span listed in the table is recommended.

Table: Using the Automatic Lock Configuration Option

#### SYS.3.2.3.M5 Using the device locking configuration option

Since it can not be ruled out that the device only short term, z. If less than three minutes are unobserved to third parties, the following recommendations are proposed for the implementation of the above measures, taking into account the criteria of the three fictitious user groups.

Table: Using the device locking configuration option

The immediate retrieval of the passcode for user groups 2 and 3 is due to the fact that confidential information could be found on the device. For user group 1, usability was a little more weighted in this example and would thus allow for the possibility of short-term unauthorized use of the telephone function.

#### SYS.3.2.3.M6 Using the configuration option "Maximum number of failed attempts"
This option determines after how many incorrect passcode entries all data is deleted from the device. If no changes have been made to the factory settings, the device enforces a blocking period after six failed attempts. Only after expiry of the blocking period, the passcode can be entered again. This blocking period is automatically extended with every further attempted failure. If the maximum number of failed attempts is equal to or less than 6, no lock-up period is enforced. When the maximum number of failed attempts is reached, data is immediately cleared from the device. Previous semi-automated attacks on the passcode assumed that no value was set to reduce the maximum number of incorrect entries allowed or that a value of ten attempts and only one passcode consisting of four numbers was used. This provides professional attackers with sufficient scope for systematically spying on the passcode. For the three fictitious user groups, the following maximum values ​​are recommended.

Table: Using the configuration option Maximum Number of Failed Attempts

#### SYS.3.2.3.M7 Preventing unauthorized deletion of configuration profiles

Depending on the MDM provider used, it is possible to store restrictions regarding the deletion of configuration profiles. So there may be the possibility that the configuration profile can never be deleted or password-based and thus authorized. Password-based authorization should adhere to the passwords established in the institution. Basically, the users should not be enabled to delete the configuration profiles unnoticed. Furthermore, it is recommended to use different passwords for securing the configuration profiles at least per user or profile group. When integrating the device into the MDM infrastructure using the Device Enrollment Program (DEP), the user is automatically unable to make unauthorized changes to the configuration profiles.

#### SYS.3.2.3.M8 Timely update of the operating system

The Apple company provides at irregular intervals new or updated versions of the iOS operating system free of charge for currently supported devices. The availability of an update is displayed to the user through the Settings app in the General Software Updates section of the Home screen in the Settings app. Those responsible must conduct a test for compatibility with the currently deployed apps and integrated infrastructure components in a timely manner. If no serious errors in usability, security and reliability can be identified, all users must be informed and prompted to update the devices within a defined time window. The table below gives recommendations for the update period and supporting measures.

Older devices that no longer provide current iOS versions must be timely removed and replaced with supported devices as part of life-cycle management. It must be prevented that no longer manufacturer-supported and updated devices are in use.

Table: Establishment of timely updates of the operating system

Since the introduction of iOS 9, it has been possible to update the operating system via the Mobile Device Management Systems.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "iOS for Enterprise".

#### SYS.3.2.3.M9 Using a complex device code
Activating the passcode denies unauthorized third parties access to the information in the smartphone or tablet. In addition, using a complex password will provide improved entropy for certain encryption keys. For the three fictitious user groups, the following values ​​listed in the table are recommended.

Since the use of special characters in passcodes has a strong impact on usability, their use should be carefully considered. The complexity can also be increased by significantly increasing the password length.

Table: Using a complex device code (passcode)

#### SYS.3.2.3.M10 Using the fingerprint sensor

For better acceptance of a complex passcode and the associated better encryption of the information on the device can be used on the use of the fingerprint sensor. When using biometric features (fingerprint) for unlocking, a potential attacker is able to remove and replicate the fingerprints on the surface of the device or objects with a smooth surface. When balancing the risk acceptance of compromising the fingerprint against better encryption and enforcing complex passwords within the institution, it should be noted that if the Touch ID is active, the rightful owner will be verified by entering the passcode after 48 hours. For this reason, it is extremely important not to pass the passcode on to third parties. Which recommended functionalities could be used considering the three fictitious user groups is shown in the following table.

Table: Using the fingerprint sensor (Touch-ID)

#### SYS.3.2.3.M11 Using non-personalized device name

Using the device name, an attacker can usually draw conclusions about the user or the institution. So the device name z. B. after Bluetooth pairing with integrated multimedia systems or handsfree in modern vehicles deposited in this. Also, after connecting to hotspots, the name of the device can be seen. For this reason, no device names related to the institution and the user should be configured to prevent the personalized profiling and guessability of typical passwords. For easy identification within the institution, it is recommended to use the asset number. To avoid accidentally changing the device name, the configuration setting listed in the table should also be implemented.

Table: Use of non-personalized device name

#### Use of Institutional Apple IDs

#### SYS.3.2.3.M13 Using the Restrictions on iOS Configuration Option

For the purpose of ensuring the confidentiality and integrity of data processed or stored on the iOS-based device, any unauthorized feature or service should be disabled. Which recommended functionalities and services should be controlled by means of configuration profiles and organizational instructions taking into account the three fictitious user groups is defined and explained in the following topic groups.

background image
Through the use of face recognition software, it is now possible, people on the screen in the lock screen z. For example, to match images from social networks, publicly accessible image galleries and the results of search engines and so to identify the user, building on this potential passwords and develop further approaches for social engineering attacks. Below are the corresponding configuration recommendations for reducing the attack surface for social engineering based on the example of a personal wallpaper that represents, for example, the user or parts of his family.

Table: Using the "Restrictions on iOS" configuration option - Background image

lock screen

The lock screen provides users with a variety of ways to view information from factory-installed apps, such as: For example, the calendar overview for today and tomorrow, the reminders, the traffic situation, the weather as well as via the widgets, the information installed from the App Store and displayed via push notification short messages available. The control center makes it possible to quickly and easily put the device in flight mode, but also to activate AirPlay for the entire device.

Table: Using the "Restrictions on iOS" configuration option - Lock screen

The safeguarding of AirPlay is subjectively deepened in the measure SYS.3.2.3.M16. Along with the release of the message center and the "Today" view, users should be made aware of the use of the information that can be acquired, and a recommendation be made as to which widgets should not be activated with which content.

Siri

Siri is used to recognize and process the language of the user, thereby enabling the functions of a personal assistant. In the case of an existing Internet connection, all voice data is transmitted via a cryptographically secured connection to servers under the sovereignty of Apple, processed on the servers, the result obtained returned to the device and offered for further processing. The following table shows an example of which configuration settings make pragmatic handling of Siri possible.

Table: Using the "Restrictions on iOS" configuration option - Siri

If there are blind and visually impaired people in the user group, the operation of the device by Siri is massively simplified or the extensive use of smartphones and tablets is made possible. The possibilities of using the device by Siri must not be confused with the functions of VoiceOver. This must be incorporated into the assessment of potential risks of confidentiality and integrity breaches.

Unified Communication

The marketing term Unified Communication (UC) summarizes all configuration recommendations for Apple's built-in apps, such as FaceTime and iMessage for video and message chats.

Table: Using the "Restrictions on iOS" configuration option - Unified Communication

Should security management already define recommendations for handling chat and video telephony applications, these recommendations should also apply to the use of FaceTime and iMessage. When using FaceTime and iMessage, all information on all devices associated with the Apple ID is displayed simultaneously in the application itself and in the message center.

Diagnostic and usage data
Based on Apple's guidance, the diagnostic and usage data may include details of hardware and operating system specifications and performance statistics, as well as information about how the device and the apps are used. Users' personal data are either not recorded at all or deleted from the reports before they are sent to Apple. In addition, if the user has agreed to provide this information to Apple and the location services are enabled, the current location of the device will also be sent. The setting values ​​listed in the table for handling diagnostic and usage data as well as location data are recommended.

Table: Using the "Restrictions on iOS" configuration option - Diagnostic and usage data

Should this recommendation be based on the established guidelines of the institution z. For example, if you deviate from Windows systems, it is advisable to have an overall evaluation of the handling of diagnostic and usage data and a consistent implementation.

Apple Watch

By linking the Apple Smartwatch to an iOS-based device, you have the option of: B. messages or emails on this and to respond directly. For integration and protection, the following two configuration options are offered.

Table: Using the "Restrictions on iOS" configuration option - Apple Watch

** Cross **

At this point, individual overarching recommendations are listed that can not be grouped directly by topic.

Table: Using the "Restrictions on iOS" configuration option - General

#### SYS.3.2.3.M14 Using the iCloud infrastructure

SYS.3.2.3.M1 defines the strategy for the use of cloud services and the associated operational, security and data protection requirements. The possibilities of centralized management of functions for using the iCloud are described below. If the use of the iCloud infrastructure has not been prohibited in principle by the institution's security management (see SYS.3.2.3.M1), a check should be made to determine to what extent the use of the following functions is compatible with the internal requirements. During the examination, the handling of the Apple company must also be incorporated with regulatory inquiries. Detailed information can be found in the document "Legal Process Guidelines" via the link stored in chapter 3.2.

When iCloud is used, Apple's two-factor authentication for iCloud access should be checked and enabled.

Which functionalities of the iCloud should be controlled by means of configuration profiles without loss of security considering the three fictive user groups is shown in the following table.

Table: Using the iCloud Infrastructure

#### SYS.3.2.3.M15 Using the continuity functions
With the AirDrop function, users can interact with other users in the vicinity, such as: For example, share photos, videos, or location information. This requires that both users use a device from Apple. The Handoff feature provides users with the ability to start a document, e-mail, or message on one device and continue to another device closer to the point where they left off. Handoff works with Apple apps such as Email, Safari, Maps, Messages, Reminders, Calendar, Contacts, Pages, Numbers, and Keynote, as well as some third-party apps. For this purpose, including the iCloud infrastructure z. Such as search queries and favorites in the Maps app, newly learned dictionary entries, the call history, podcast app playback positions, Safari's Safari tabs, its RSS subscriptions, iBooks app bookmarks, the VIP list in the Mail app and HomeKit settings synchronized across devices.

Both features require an active Apple ID for this. With the Handoff function, the devices used must be linked to the same Apple ID. This means that the settings suggested here must correspond to the settings for the iCloud.

Table: Using the Continuity Functions

#### SYS.3.2.3.M16 Using the configuration option for AirPlay

AirPlay allows users to stream their music, photos, and videos to an AirPlay receiver, such as Apple TV. Another application for AirPlay is the screen synchronization between an iOS-based device and the Apple TV. Screen synchronization via AirPlay makes it very easy to integrate the user and guest devices in the institution's conference rooms. The configuration examples below provide an optimal trade-off between user flexibility requirements and the institution's internal security policy for the three fictitious user groups.

Table: Using the configuration option for AirPlay

By adding configuration profiles for user groups 2 and 3, which by whitelisting and storing passwords limit the allowed AirPlay goals, a reasonable compromise between usability of the devices and security of the institution's information is realized for these users.

#### SYS.3.2.3.M17 Using the device code history

For the three fictitious user groups, recommendations are given for the purpose of maintaining the confidentiality of the passcode used and preventing it from being repeated too quickly by the user in the table below. When establishing the value, the established rules within the Windows domain or similar can be used for better acceptance.

Table: Using the device code history

For user group 1, it was possible to repeat the first original password after the fifth change. Taking into account the maximum passcode validity (see SYS.3.2.3.M3), the repetition of the first passcode of the user is thus possible after 600 days.

#### SYS.3.2.3.M18 Using the configuration option for the Safari browser

With the iOS operating system, Apple ships the preinstalled Safari browser with the option of customization through configuration profiles. The in-depth implementation of the browser app makes it possible to adapt the behavior of the browser to the internal requirements of the institution. The following table lists recommendations for customization, taking into account the three fictitious user groups.

Table: Using the configuration option for the Safari browser

#### SYS.3.2.3.M19 Using the filter option for web pages
Regardless of the institution's permanent involvement in the institution's proxy and reputation infrastructure, Apple provides the ability to create filter lists for permitted URLs (which are a complement to the previously pre-selected URL groups), whitelist URLs, blacklist URLs, and the External integration of third-party content filters. Contrary to the previous measures, no general recommendation can be made at this point; rather, the use of the individual options per user group is shown.

Table: Using the filter option for web pages - general

If a reputational service or a proxy infrastructure is already offered by those responsible in the IT, the iOS-based devices can be integrated by depositing a global HTTP proxy for all installed browsers. To use a global proxies, the apps must initiate an NSURL call. An integration of the devices into the internal proxy infrastructure must take place either permanently or based on the used apps in the infrastructures by means of a VPN connection. The following HTTP proxy configuration options can be used to deposit a global proxy.

Table: Using the Filtering Option for Web Pages - Proxy Configuration Options

The configuration options for integrating the devices via a VPN dial-in are named in the action SYS.3.2.3.M20.

#### SYS.3.2.3.M20 Integration of the devices in the internal infrastructure via VPN

For the purpose of maintaining the confidentiality and integrity of the information of the institution, the iOS-based devices should be integrated into the institution's infrastructure via VPN. For the configuration of the VPN connections to the servers of Aruba VIA, Checkpoint Mobile VPN, Cisco AnyConnect, F5 SSL, Juniper SSL, SonicWALL Mobile Connect, NCP, Genoa or SINA, the MDM providers can rely on Apple with the VPN manufacturers resort to coordinated settings. However, in addition to the configuration profile in some cases additionally the apps of the VPN server manufacturer, z. For example, the F5 BIG-IP Edge Client, Junos Pulse, Cisco AnyConnect, and Aruba Network VIA app can be installed from the App Store. Recommendations are made in the document "Technical Guideline TR-02102" of the BSI for the use of IPSec and SSL / TLS (see chapter 3.2). When implementing the VPN, regardless of the algorithm and protocol used, it is possible to configure a VPN permanently, only when needed or for individual managed apps.

** ** Permanent

A permanent VPN allows full control over all communication links. In-house administrators can then fully monitor and filter traffic to and from iOS-based devices to protect the institution's information and regulate device access to the Internet according to internal needs.

** VPN On-Demand **

With VPN On-Demand, iOS-based devices can automatically establish a VPN connection to the institution when needed. VPN On-Demand requires authentication regardless of the certificate-based protocol used. The VPN On-Demand configuration profile must be configured with the OnDemandRules key in a VPN payload. The rules for recognizing demand are in two stages, network discovery and connection evaluation.

** App-based VPN **
An app-based VPN allows any MDM managed app to communicate with the systems in the institution via a tunnel. All unmanaged apps are prohibited from using the tunnel in the institution. Another feature of managed apps is that different VPN connections are configured to protect information in more detail. To implement an app-based VPN, the managed app must be accessible through standard network APIs.

A general recommendation can not be made at this point, since the need for protection, the algorithms and authentication methods used as well as the existing DNS structure must be taken into account when deciding whether or not to use a variant.

#### SYS.3.2.3.M21 Sharing apps and integrating the Apple App Store

The added value of iOS-based devices usually only arises when a smartphone or tablet is an integral part of the institution's infrastructure and, as a result, provides users with extensive access to the information. This means that internal data (usually data with a confidentiality classification) outside the institutional infrastructure must be made available to users on their devices. The iOS platform is closed in itself and Apple controls all programs (apps) before sharing in the App Store. Despite this control, it can not be ruled out that the apps will leak confidential or internal information. As part of the release process, at least the following criteria should be reviewed and used as the basis for a rejection or release:

* Is the app unauthorized accessing user information?

 
+ Is the app trying to gain unauthorized access to the device's geo data?
+ Is the app trying to access the address book without authorization?
+ Is the app trying to access the device's clipboard without permission?
+ Is the app trying to detect unauthorized which apps are still installed on the device?

 

* Is the app trying to redirect the communication connections without authorization?
* Is the storage of app application data outside the German or European data protection area?
* Is the storage of app application data automated or unsolicited on servers outside the jurisdiction of the institution?
* Is there a risk of user profiling by non-ad-free apps?
* Is the data within the app automatically decrypted when the device is unlocked, or does the user need to enter a password to decrypt?
* Does the app offer its own sharing services or network interfaces?
* Are there updates to the app developer regularly?
* Does the app developer implement the latest interfaces and policies from Apple?
Taking into account the results of the approval process and independent of the use of the enterprise volume licensing program (VPP), the following configuration options and their use may help to support the security objectives per user group.

Table: App Store Integration and Apps Sharing

### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.3.2.3.M22 Enforcement of compliance requirements (CI)
The detection of manipulation of the operating system is not fully possible by querying an Apple-enabled interface. The detection of violations of internal rules of the institution should be ensured by the MDM framework of the respective provider. Depending on the quality of the jailbreak obfuscation, this can be recognized, but it can be assumed that the detection rate is low. If there is a suspected breach of regulations or manipulation of the operating system, the actions previously configured by the responsible administrators should be carried out independently. Due to the different implementation variants of the individual MDM providers, there is no possibility to pronounce a generally valid configuration recommendation.

#### SYS.3.2.3.M23 Using Automatic Configuration Profile Deletion (CI)

By depositing a special expiration date or expiration interval (days and hours), configuration profiles stored on the device can be automatically deleted without the need for an otherwise required Internet connection, thus ensuring that, for example, a VPN connection to the institution is no longer possible. However, this method should only be used if the user basically only needs temporary access to information with increased protection requirements. If information with high protection requirements is stored on the device, this methodology can also serve as a preventative measure for verifying and ensuring the legitimate user / owner.

#### SYS.3.2.3.M24 Use of location-based policies (CI)

An example of a geofencing request could be that the deployed devices are not allowed to leave the premises of the institution and a warning is sent to the user, the responsible administrators and the security management upon leaving. Due to the time delay, the user has the opportunity to go back to the institution's premises with the device and thus prevent a deletion of the information or the device. By actively notifying the security management, they can detect the security incident, train their own users through awareness-raising measures and, in the event of a theft, ensure that relevant information does not leave the premises of the institution. This type of protection of the information with high protection requirements could also apply to legal territories such. B. the area of ​​the Federal Data Protection Act or the European Data Protection Space. However, the use of geofencing policies must not violate internal and legal requirements. A possible institution-internal evaluation of location-based data is to be excluded organisationally or coordinated with the Staff Committee.

#### SYS.3.2.3.M25 Using the configuration option for AirPrint (CI)

On the part of the Apple company, the AirPrint functionality was firmly integrated into the operating system. This feature can not be turned on or off. The responsible administrators should provide the AirPrint printers released in the institution through a configuration profile to the user. Furthermore, when assessing and approving AirPrint printers in the institution, it is recommended that they be integrated into their own network segment. Only through its own network segment, it is easily possible to apply for a custom firewall rule through the approval process, to manage the multicast communication on port 5353 (Bonjour, mDNS) within the network segment and the Internet Printing Protocol (IPP) on the limit required IP addresses or network segments. To do so, it must be ensured that all communication links are always routed through the institution's infrastructure systems.

#### SYS.3.2.3.M26 No connection with host systems (CI)
To create a local backup, the device must be connected to iTunes via USB cable or Wi-Fi. When using Wi-Fi, an attacker may attempt to unnoticeably perform a man-in-the-middle attack and take control of the information on the device. With a local backup, whether encrypted or unencrypted, anyone with host access can make a copy of these files almost unnoticed, then decrypt this copy made and analyze the existing information, especially the user behavior. Another risk in linking the iOS-based device to a host (PC or notebook) is the local filing of a valid pairing key on the host. An attacker could use the pairing key to extract sensitive information from the iOS-based device for a period of time without knowing the passcode. To prevent the named attack scenarios and the loss of sensitive information, the responsible administrators should not be able to connect to host systems.

#### SYS.3.2.3.M27 Using the configuration option for APN

This configuration option determines how iOS-based devices connect to the wireless network. This means that with wrong settings there is no way to establish a data connection. Currently APN usernames and passwords with up to 64 characters can be defined in the configuration profile. By using an institution-based APN, it is possible to limit the possible range of IP addresses and include this restricted IP address range in the firewall rule processes and circuits.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Further information on threats and security measures in the "iOS (for Enterprise)" area can be found in the following publications, among others:

*

 #### [AppAGB] Terms and Conditions for iTunes

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/internet-services/itunes/de/terms.htm> l

  

 
*

 #### [AppAGBCl] Apple Terms iCloud

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/internet-services/icloud/de/terms.html>

  

 
*

 #### [AppAGBGC] Terms and Conditions for Game Center

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/internet-services/itunes/gamecenter/de/terms.html>

  

 
*

 #### [AppCon] Appel Configuration

  

 Apple, (last accessed on 27.09.2017)
 <Https://support.apple.com/de-de/apple-configurator>

  

 
*

 #### [AppDS] Apple Privacy Policy

  

 Apple (last accessed on 27.09.2017)
 <Https://www.apple.com/legal/privacy/de-ww/>

  

 
*

 #### [AppleSec] Apple Security Updates

  

 (last accessed 05.10.2017)
 <Https://support.apple.com/en-us/HT1222>

  

 
*

 #### [AppLPG] Apple's Legal Process Guidelines

  

 Apple, 06.2017
 <Https://images.apple.com/legal/privacy/law-enforcement-guidelines-outside-us.pdf>

  

 
*

 #### [AppSiup] Apple security updates

  

 Apple (last accessed on 27.09.2017)
 <Https://support.apple.com/de-de/HT201222>

  

 
*

 #### [AppSupp] Apple Support Website

  

 (last accessed 05.10.2017)
 [https: // www.apple.com/support](https://%20www.apple.com/support)

  

 
*

 #### [AppTwfac] Apple Two-factor authentication for Apple ID

  

 (last accessed 05.10.2017)
 <Https://support.apple.com/en-us/HT204915>

  

 
*

 #### [AppViPro] Discontinued and vintage products

  

 Apple, (last accessed on 27.09.2017)
 <Https://support.apple.com/de-de/HT201624>

  

 
*

 #### [DEP] Device registration program

  

 Apple, (last accessed on 27.09.2017)
<Https://www.support.apple.com/de-de/HT6578>

  

 
*

 #### [Support] Support for businesses and educational institutions

  

 Apple, (last accessed on 27.09.2017)
 <Https://www.apple.com/de/support/business-education/>

  

 
*

 #### [TR21022] BSI Technical Guideline, Cryptographic Procedures

  

 Use of Transport Layer Security (TLS), Federal Office for Information Security (BSI), 2017
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)

  

 
*

 #### [VPP] Volume License Program

  

 Apple, (last accessed on 27.09.2017)
 <Https://vpp.itunes.apple.com/de/store>
