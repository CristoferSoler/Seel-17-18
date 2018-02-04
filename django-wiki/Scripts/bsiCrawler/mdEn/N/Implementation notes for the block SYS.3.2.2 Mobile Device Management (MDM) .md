[toc]
 
1 description
--------------

### 1.1 Introduction

In a constantly more digitized work environment, institutions supplementing or even replacing the notebook provide their employees with further mobile-working facilities through mobile devices. This usually goes hand in hand with the fact that employees want to have permanent access to internal and external sources of information when they are on the move and also want to use the devices for relaxation and further education.

Whether an institution wants to address the opportunities and risks of mobile devices is no longer relevant today. Because with high priority, the question must be answered, whether this dispute has not already occurred or when this happens. If an institution fundamentally decides against mobile devices, then at least the risks that could arise through the use of and interaction with private devices are to be considered.

Mobile terminals are fundamentally different in procurement, operation and use than a workstation PC or server. In order to operate such devices safely, it is essential to understand these differences and to incorporate this understanding in the decisions about processes and procedures.

For example, workstation PCs and servers can be purchased and then equipped with any operating system. The administrators can thus completely customize the devices. This is different with mobile devices. Here, the hardware is purchased along with an operating system, and with few exceptions, only the operating system provided by the manufacturer works on these devices. Thus, the institution can not control the mobile devices as usual. Even if a mobile device management (MDM) system is used, the manufacturer always has some control over the device because it controls the operating system.

Also new to the operating processes is that it is no longer up to the user alone to determine updates, as the device manufacturer controls this process. For Android-based devices, the mobile service provider is often involved in this process as it often adjusts the manufacturer's updates and then passes them on to their customers.

The mobile service provider is an important partner for the operation of mobile devices. He not only controls the data connection to the devices, but he also configures them depending on the contract or terminal. Any mobile device with a SIM card is thus potentially remotely controlled by the mobile operator.

For the illustration of the different implementation recommendations, the following three fictive scenarios are used in this document.

**1. Scenario**

* Users mainly use their devices to make phone calls and send e-mails.
* Users can not access internal collaboration and document management systems.
* The information is not classified as confidential.
** 2nd Scenario**

* Users use their devices to talk on the phone, send emails, and process business documents.
* Users can access internal collaboration and document management systems.
* Sometimes the information is classified as confidential.
** 3rd Scenario**

* Users use their devices to talk on the phone, send emails, and process business documents.
* Users can access internal collaboration and document management systems, financial data or critical systems of the institution.
* Sometimes the information is classified as strictly confidential.
### 1.2 Life cycle

** planning and conception **
In the planning and design phase, all possible usage scenarios, eg. For example, integration into a collaboration solution, access to merchandise management systems and the maximum protection requirements to be implemented, will be included in the selection of the central management solution (see SYS.3.2.2.M1 Definition of a Strategy for Mobile Device Management). If private and business areas need to be strictly separated, it is advisable to contrast whether this can be achieved using operating system mechanisms such as managed apps and managed open-in, through a container solution or even through virtualized user environments. It should also be examined at this stage how the mobile devices can be integrated into the information and communication infrastructure in a user-related manner. From the results, new requirements can be derived for the previous network segmentation, the security gateway infrastructures and their functions.

In the planning and design phase, the institution has to decide which operating model or combination of the two models should be implemented: * devices issued to employees * or * bring your own device (BYOD). * On this basis, the security requirements for mobile devices are technically and organizationally implemented.

Another very important question is the extent to which users may or must install their own apps on their mobile device, whether the employees themselves may add additional apps for private use and whether they will take over part of the administration themselves.

Based on the protection needs of the information (compare also the three fictitious scenarios) and the possibilities of IT operation, an MDM solution should be chosen (see SYS.3.2.2.M3 Selection of an MDM product), which ensures that the data the institution are secured in accordance with the internally documented requirements.

The operating model of the future MDM solution is to be selected depending on the protection requirements of the mobile devices. A separate company, in which the servers of the MDM solution are installed in their own premises and thus including the data contained under the control of the institution, is possible with all solutions. Almost all MDM providers also offer their solutions as a cloud variant, where the software is operated on the servers of the respective provider and the customer receives a web access, with which he can manage the applications and linked mobile devices.

**Procurement**

In the procurement of an MDM solution as well as in the selection of mobile end devices and the mobile radio provider, safety aspects should also be considered in addition to the economic aspects. Here is much possible, for example, a full service offer with a mobile service provider, which includes devices, mobile phone contract and mobile device management, or the simple purchase of equipment and a fully self-administered operation.

The offers of the mobile service providers are interesting for the security of the devices insofar as it is possible here to operate the devices in a closed user group. The mobile devices then receive via mobile phone no regular Internet access, but are summarized by the mobile operator in a network in which only the devices of the institution.

If employees receive mobile devices from the institution, they should be centrally procured and sufficiently meet internal security requirements.

**Implementation**

Depending on what is specified in the concept, employees must have access to a self-service kiosk for setting up their own devices, or the administrators of the institution must completely configure the mobile devices for the employees.
In Chapter 2, recommendations for action are presented on the basis of the three scenarios defined in the introduction. Regardless of the method by which the configuration profiles are rolled out to the managed devices, it must be ensured that users can not delete the protection profiles without authorization.

**Business**

To ensure that mobile end devices can be used properly and reliably, the MDM solution used must pass technical security specifications to the devices (see SYS.3.2.2.M4 Distribution of the basic configuration to mobile devices). The most important tasks for the responsible persons are to carry out regular safety-related maintenance measures as well as to administer user accounts and authorizations securely. In addition, the systems of the MDM solution should be specifically monitored in order to be able to quickly identify availability problems and security incidents.

As with all IT systems, a well-functioning change management system is also a key element for the servers of the MDM solution in order to maintain system security.

** ** segregation

The MDM solution must not be shut down without prior notice. If it is to be taken out of service, the affected users must be informed in good time.

When eliminating the server of the MDM solution, it must also be ensured that there is no longer any information worth protecting on the hard disks. It is not enough just to reformat the disks, but they have to be completely overwritten at least once. With flash memories, the internal memory blocks can not be addressed directly due to their design. That is, to clear the data, the resetting functions of the controller must be used. If information with a high protection requirement has been processed or stored on the server of the MDM solution, the destruction of the flash memory according to DIN 66399 "Destroying data carriers" is probably the safe method.

The segregation of a server or the complete MDM solution must be documented. Inventories and networks must be updated. Insofar as the information network changes structurally as a result of the separation, the security concept should also be adapted accordingly.

** Emergency Preparedness **

As with all other central IT systems, an appropriate contingency plan must be prepared for an MDM solution. A central element of emergency preparedness is data protection, which should also include relevant areas of the operating system and security management. In the case of increased requirements for the availability of the MDM solution, redundancies can additionally be provided for.

As part of the emergency preparedness arrangements should be made in a cloud solution with the contractors corresponding agreements regarding the MDM solution used.

2 measures
-----------

The following are specific implementation notes in the Mobile Device Management (MDM) area.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### SYS.3.2.2.M1 Definition of a strategy for Mobile Device Management

The basis for all further steps is the definition of a strategy that determines how employees can use mobile devices based on the information to be processed and their protection needs, and how the devices are integrated into the internal structures of the institution. Such a strategy should include at least the following points.

** May the MDM be run as a cloud service? **
If cloud services are used, legal aspects must always be taken into account if personal data are transferred in the meaning of the Federal Data Protection Act (BDSG, § 3 (1)). Such order data processing, depending on the actual location of the data, is only possible under certain conditions (§ 11 BDSG) and also bound to a written order. If institutions do not stick to it, they violate existing law. As a result, they not only damage their reputation, but can also face claims for damages or fines.

If the data protection requirements can be met by the service provider and the institution, then it should be checked whether the internal business and security-relevant requirements can be met in the case of a cloud solution. Here u. a. consider the location of the MDM provider.

** Should the MDM be operated by the institution itself? **

In order to be able to answer this question, it is recommended in the first step to determine your own requirements regarding the economic, security and data protection requirements. It is also important to answer the question of how critical it is for the institution if the MDM is partially or completely canceled. Would such an emergency be manageable? Can security incidents be detected and dealt with professionally?

The next step should be to decide whether to integrate an internal directory service and what needs to be met.

** Which compliance requirements must be enforced? **

If violations of internal regulations of the institution are to be recognized and automated actions are carried out, compliance requirements must be enforced on the mobile devices of the institution. The response to compliance violations can vary, as it depends on the protection needs of the information and the implementation variant (* devices of the institution * or * BYOD *). Once the need has been determined, the strategy should formulate a technical implementation that meets compliance requirements for procurement and design.

** Which mobile devices and which operating systems must support the MDM? **

In order to achieve high productivity and to support the safety-conscious handling of the users, it is recommended to make use of the existing experience of the employees with mobile terminals of the institution. The following questions should help those responsible to determine the need for the strategy:

* Are mobile device users allowed to access institution information using the preferred device? Should this be done independently of which operating system it is operated on?
* Should users be able to search for and install applications in the institution's own app store to access confidential information?
* Should private and business information of the institution be separated and managed on the mobile device? Should this be done without affecting the existing experience of employees with mobile devices of the institution?
* Should highly effective security measures be implemented that are invisible to the user of the mobile device?
* Should users be supported in meeting the institution's requirements with freely selectable mobile devices and the resulting better acceptance of implemented technical safeguards?
* What is the administration overhead if operating systems from different manufacturers are supported in various versions?
** Does the MDM solution have to be multi-client capable? **
A multi-tenant MDM solution is unlikely to be necessary for smaller environments with fewer users. However, for a large number of users, the desire for separate clients can quickly arise for different reasons. Whether or not a multi-client MDM solution is necessary depends on how complex complex authorization structures can be mapped within the solution. For the user of a mobile device, without this possibility, the best MDM solution may be worthless, since each submitted authorization is automatically inherited by all and thus follows the maximum principle. If organizational structures are to be mapped, this is a clear indication of the need for a multi-client MDM solution. In order to be sustainable, the solution should then work in the hosted version as well as in the cloud variant.

A multi-tenant solution may also be useful if you want to provide access to the back end of the MDM solution for different stakeholders, such as: For responsible administrators, auditors, internal audit or controlling.

** Do cloud services have to be integrated? **

When using online storage services (eg cloud services from Microsoft, Google or Apple, Dropbox and similar), a distinction can be made between different variants. Online backup, where data is stored once or at regular intervals over the Internet in order to be retrieved after a loss of data, represents the simplest form of use. In the so-called online hard disk depending on the service provider pure data storage also additional functions available. For example, data and documents can be shared or shared with employees or business partners, and synchronized across multiple devices.

If the data of the institution can not be accessed because the online storage service is not available due to a failure of the service provider or the connection to the service, this can disrupt the business processes or they can completely fail. In particular, the protection requirements for the information concerned are important. If the processes have to be highly available, financial losses or damage to the image may be the result of longer downtimes of the online service. In addition to the availability of the online storage and the information stored therein, especially the confidentiality of the information has a high priority. Attackers are able to access confidential information of the institution and this z. B. make it accessible to a wider group of people threatened image loss as well as legal consequences and financial losses.

When information is transmitted, edited, or finally stored over the network, integrity problems can occur that can even lead to total loss. This also applies to encrypted data. Such problems have a similar effect as the loss of confidentiality.

If at the end of the contract the information of the institution is not properly deleted by the provider of the online store, there is a risk that unauthorized persons may access this information.

** Do document management systems have to be integrated? **

The question of whether to integrate document management systems is closely related to the multi-client capability requirement of the MDM solution. For the strategy, this means that the MDM solution must be able to pass information to other enterprise systems. Eg via web services. Here it must be ensured that this is scalable and independent of the number of other integrated systems.

** Do peripheral devices have to be integrated and managed in addition to the mobile devices? **
When mobile devices are introduced, those responsible must also define the data protection, safety and operational requirements for the integration of peripheral devices. For example, it is often far from easy to implement a mobile printing strategy within the institution, taking into account the different locations of mobile devices. The reason for this is that within most institutions, a wide range of hardware, software, and service offerings must be considered, depending on the printer and the underlying printer infrastructure.

Using integrated solutions in the operating system becomes more difficult the more mobile platforms are supported. Should z. For example, if existing network printers can be reached via the mobile devices, partner solutions of the MDM providers usually have to be integrated or cloud-based solutions must be used. Evaluating which solution best supports the institution's security strategy should be an integral part of the planning and design phase. If this is forgotten at this point, it can be expected that the users of mobile devices will build up "workarounds" that bypass the established security measures.

** Which operating model should be considered for mobile devices? **

One of the most important questions when using mobile devices is which operating model should be introduced. Two operating models or a combination of both models are available:

* Equipment Issued to EmployeesIn this model, the institution procures the equipment itself and makes it available to users, either as a stand-alone or shared device.
* Bring Your Own Device (BYOD) Employees of the institution use existing private mobile devices to access information from the institution.
Whether BYOD can be approved within the institution should be answered and evaluated based on the following questions regarding acceptable risk.

* Are the legal conflicts in the use of private mobile devices with regard to the software license right clarified or resolved, eg. B. professional use of private licenses or private and professional use of official licenses?
* In the context of emergency management, have measures been agreed with the owners of the mobile devices with regard to the deletion of the entire database?
* Are IT managers able to test every single private device for its suitability for institutional deployment?
* Have options been evaluated on how to properly implement internal privacy and security requirements?
* Is it ensured that unauthorized third parties can not access information about the institution when repairing and maintaining private mobile devices?
* Is it ensured that after an employment relationship has been terminated, the former employee can no longer access information from the institution and all official information on the mobile device can be deleted?
* Is it ensured that enough resources are available for user support at all times?
Should one of the questions be unworkable, ie be answered with no, the use of BYOD is at least not recommended for the scenarios 2 and 3 mentioned in the beginning.

The strategy for the Mobile Device Management must be fixed in writing and approved by the ISB. It should be updated regularly.

#### SYS.3.2.2.M2 Setting Allowed Mobile Devices
In principle, all mobile devices used in an institution must meet the requirements of the MDM strategy. This means that they must support all technical security measures that the institution has already implemented or intends to provide in the foreseeable future. For the acquisition of mobile devices, whose displays and batteries have been claimed to be highly stressed, a device life cycle of about two years should be estimated. If devices from different manufacturers and with different operating systems are provided, it must be ensured that the security of the information network and the processed information is not jeopardized by different configuration profiles.

The MDM may only grant mobile devices access to internal networks that have undergone the approval and validation process. There must be an overview of the mobile devices and operating system variants that are allowed in the institution.

#### SYS.3.2.2.M3 Selection of an MDM product

There are a variety of MDM products on the market. An MDM product must be selected that supports the defined requirements of the MDM strategy. It must be ensured that only MDM software is used or procured that can implement all technical and organizational security measures and supports all shared mobile devices.

#### SYS.3.2.2.M4 Distribution of the basic configuration to mobile devices

Those responsible must ensure that all mobile devices, regardless of the manufacturer, model, and operating model, immediately receive the selected configurations through the MDM, including security settings. To ensure that all information of the institution on the device is protected by the safeguards, all mobile devices should be in factory condition.

The requirements and recommendations for the basic configuration and integration of mobile devices to be observed can be found in the implementation notes of the following modules:

* SYS.3.2.1 Smartphone / Tablet
* SYS.3.2.3 iOS (for Enterprise)
* SYS.3.2.4 Android
* SYS.3.2.5 Windows
* SYS.3.2.6 BlackBerry
#### SYS.3.2.2.M5 Secure basic configuration for mobile devices

The basic configuration of the devices must be appropriate to the protection requirements to be met and is usually defined in a specific device block. The requirements and recommendations for the basic configuration and integration of mobile devices to be observed can be found in the implementation notes of the following modules:

* SYS.3.2.1 Smartphone / Tablet
* SYS.3.2.3 iOS (for Enterprise)
* SYS.3.2.4 Android
* SYS.3.2.5 Windows
* SYS.3.2.6 BlackBerry
Taking into account the established processes for the commissioning of mobile devices and the transfer to the later users, it should be ensured that the MDM client already exists on the devices or the users are able to install it themselves.

#### SYS.3.2.2.M6 logging

In order to realize a logging in an information network, it must be planned how it will be constructed technically and organisationally. Also, a security concept must be created. If a security concept for logging already exists, the requirements for the MDM should be integrated there. It also has to be regulated how the access rights to logging services and log data of the MDM are granted.

When logging centrally, consider how to integrate the central logging server into the network infrastructure of the information network or access it from a cloud solution. The following tables show which setting recommendations could be used to map the logging in the MDM for the mobile devices.

Table: Logging in MDM - Security
Table: Logging in MDM - App Management section

Table: Logging in MDM - Content Management

Table: Logging in the MDM area Device Restrictions

Table: Logging in MDM - Troubleshooting and Monitoring

Table: Logging in MDM - Mobile Device Enrollment

The MDM must also log all security-related actions and configuration changes to the MDM itself. The log files must not be viewed by unauthorized persons and can not be changed. When logging, legal and internal regulations must be adhered to.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the area of ​​"Mobile Device Management (MDM)".

#### SYS.3.2.2.M7 Select and share apps

The added value of a mobile device is only recognizable when it becomes an integral part of the institution's infrastructure and gives users full access to the information. This means that internal and / or confidential information is also made available to users outside of the institutional infrastructure. As part of the approval process for apps, therefore, at least the following criteria should be reviewed and used as the basis for a rejection or release:

All shared applications (apps) should be made available to users internally in a standard catalog and thus published. If the manufacturer of a mobile device offers volume licensing programs for its platform, this program should be integrated into the software distribution processes.

Taking into account the results of the approval process, the safety recommendations for each scenario can be supported by means of the following recommendations.

Table: App Store Integration and Apps Sharing

#### SYS.3.2.2.M8 Definition of permitted information on mobile devices

The institution should determine the conditions under which mobile devices may process which information. The definition must refer to the classification or protection needs of the information or its underlying processes and to clearly define the conditions for processing, such as: Encryption, containers, or shared with the cloud. This definition should be used as the basis for the MDM's configuration of the mobile devices and for any additional security infrastructures needed. All regulations should be documented for the users and handed over in a suitable form. In order to automatically detect security incidents, technical measures should be implemented as far as possible, with which the established internal rules can be enforced.

#### SYS.3.2.2.M9 Selection of security apps

Perhaps the most important aspect of choosing security apps is usability. So the users should be able to quickly authenticate and quickly access apps and information of the institution via a mobile device. Any applications that increase the security of the device itself or the information stored there are assigned to the Security Apps category. The most important security app is the client of the mobile device management system. Depending on the selected operating system and the security framework of the manufacturer, there are other apps in this category whose function can be part of the MDM client:

* Apps to locate the device in case of loss,
* Anti-virus apps,
* Apps for the cryptographic protection of individual data or folders,
* Apps for deploying workspaces using a container isolation technique as well
* Apps that additionally regulate access to other apps.
Based on the chosen strategy, the selection of security apps must be formulated and regulated in a binding manner. The selection must list suitable apps for each operating system of the devices used. The MDM must force the installation of these apps.

#### SYS.3.2.2.M10 Secure connection of mobile devices to the institution

If an institution-specific access point name (APN) is used on the basis of mobile radio, this can form the basis for limiting the permitted pool of devices. All of the institution's mobile devices using this APN will be provided by the wireless service provider with an IP address range coordinated with the institution. To avoid security incidents caused by too short passwords for authentication, a complex password (up to a maximum of 64 and at least 10 digits) should be agreed with the mobile service provider. When using an institution-related APN, it should also be authenticated using the CHAP protocol.

The secure connection of the mobile devices to the institution should be done with a VPN, as this ensures the confidentiality and integrity of the information transmitted between the mobile devices and the IT network of the institution. For example, to configure the VPN connections to the servers of * Aruba VIA *, * Check Point Mobile VPN *, * Cisco AnyConnect *, * F5 SSL *, * Juniper SSL *, * SonicWALL Mobile Connect *, * NCP *, * Genoa * or * SINA * MDM vendors often provide settings tuned to VPN vendors. However, in addition to the configuration profile for the VPN connection, the apps of the VPN server manufacturer from the respective app store often have to be installed. Recommendations for the use of IPSec and SSL / TLS are made in the document * Technical Guideline TR-02102 * of the BSI (see chapter 3.2 of the TR).

When implementing a VPN, regardless of the algorithm and protocol used, it is possible to configure a VPN permanently, only as needed or for individual managed apps.

** Permanent VPN **

A permanent VPN makes it possible to control all communication connections. The people in charge of the institution can then fully monitor and, if necessary, filter traffic to and from the mobile device. This can protect the information of the institution and the access of the devices to the Internet can be regulated according to the internal requirements.

** VPN On-Demand **

With VPN On-Demand, mobile devices can automatically establish a VPN connection to the institution. The stored arrangements for the recognition of the demand by the mobile terminal usually take place in two stages, the network recognition and the connection evaluation.

** App-based VPN **

An app-based VPN is implemented differently depending on the operating system and MDM manufacturer. All solutions have in common that these apps have to be manageable. All unmanaged apps are not allowed to use the VPN tunnel in the institution. Another feature of managed apps is that different VPN connections can be configured to further protect information. To realize an app-based VPN, the managed app must be accessible through standard network APIs or be encapsulated by the MDM manufacturer with an additional layer.

Which of the described VPN variants is used depends on the protection requirements, the algorithms and authentication methods used and the existing DNS structure.

#### SYS.3.2.2.M11 Authorization Management in MDM
Permissions may only be set up in a restricted way and task-oriented according to the principle of least privileges. Identity and authorization management in the MDM ensures that users of mobile devices and administrators are only assigned the necessary authorizations. A documented way to assign, change, and revoke privileges allows you to control how information is accessed. With corresponding background systems, activities that have taken place can also be stored and evaluated. In case of damage or due to legal requirements, activities can be evaluated and assigned to those responsible.

First, determine how to organize the administrative tasks, such as helpdesk support, stand-alone user registration, or device configuration management. The responsible persons must document the functions determined for the MDM deployment. Afterwards the separation of functions has to be defined and substantiated. D. H. which functions are not compatible with each other and may not be performed simultaneously with the user account created for this purpose.

To determine the required function separations and authorizations, the following example questions can be used:

* How many levels of support are needed in the help desk?
* Which users with which mobile devices are managed by which group of administrators?
* Who develops and manages the institution's own apps?
* Who manages the policy and configuration processes?
* Which information on the mobile device or the information on it can the administrators access?
* Do internal audit or external auditors always need access to the MDM solution?
* Does security management always need access to the MDM solution?
Requirements for this may result from the tasks themselves or from legal or internal requirements. The established authorization management must be regularly checked to ensure that the allocated rights still correspond to the tasks.

#### SYS.3.2.2.M12 Hidden MDM operating environment

An MDM solution operates on IT systems that are either the sole responsibility of the institution or that are operated by an outsourcing partner on behalf of the institution. In both cases, the institution is responsible for securing the MDM components and assigning network segments as needed. Also, those responsible must ensure that the supporting IT systems for the MDM are adequately protected in accordance with the identified protection requirements. It should be noted that the security of mobile devices is directly dependent on the security of the MDM. To ensure adequate protection, the following requirements should be met:

* the operating system of the MDM solution is hardened,
* the administrative accesses are controlled,
* Abusive access is detected and appropriate countermeasures are taken,
* securing the client-server communication corresponds to the required protection requirements,
* the user credentials are protected according to the required protection requirements,
* a continuous vulnerability assessment has been established
* The MDM solution is fully integrated with the established update and change management processes.
### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).
#### SYS.3.2.2.M13 Restricting the app installation via whitelist (CIA)

In the case of increased protection requirements, users of mobile devices should only be allowed to install apps that have been examined and approved by the administration and security management of the institution (see SYS.3.2.2.M7 * Selection and Sharing of Apps *). The MDM should prevent the installation of other apps or alternatively remove unauthorized installed apps immediately.

#### SYS.3.2.2.M14 Using external reputation services for apps (CI)

A reputation service is an external service that examines apps according to specific criteria and provides the results. The reputation service is mostly based on the following three phases.

** Catalog the Apps **

The App Reputation Service collects and catalogs millions of apps from manufacturers 'stores, third-party Web sites, app-sharing services, and app reputation service providers' strategic partners.

** Analysis of the apps **

Through a multi-level, usually mostly automated analysis process, detailed information about the behavior of the apps is collected.

** Rating and rating of apps **

Each app is classified and rated. Afterwards, the evaluated app is assigned a score by the reputation service provider. To facilitate the assessment of the app, it is often assigned to one of the following fine granular categories:

* malicious,
* unwanted (unwanted),
* Suspicious,
* Moderate,
* benign (Benign) or
* trustworthy (Trustworthy)
If the users are allowed to install apps and the responsible administrators can not create a whitelist with allowed apps themselves, a reputation service can limit apps to at least category-based. However, those responsible must coordinate closely with the institution's security management.

#### SYS.3.2.2.M15 Use of PIM containers (CI)

To prevent espionage apps or unauthorized third parties from viewing or modifying Personal Information Manager (PIM) data (such as Exchange, Domino, Groupwise) on the mobile device without authorization, a PIM container should be used. Such a container encapsulates the PIM data and functions of the application to be protected from other apps on the mobile device. The container must be protected by its own password and must contain data encryption independent of the operating system and transport encryption. When deploying a PIM container, the institution's officers must ensure that the operating system of the mobile device does not present security vulnerabilities that compromise the required security.

#### SYS.3.2.2.M16 Use of Separate Work Environments (CI)

A particularly high protection of the information against dangers, which arise through the private use of the device, offer separate working environments. If there is a high need for protection and users use different apps that need to communicate in different ways with the institution's IT systems, a separate work environment should be used. Because these environments often have their own encrypted storage and VPN channel, they provide the apps with an area where the protection of the data is provided by the work environment. So also unsafe apps can be used. Separate work environments are especially recommended when apps on the device require interaction with other apps, as any communication between each app may be exploited by other apps and may become an attack gate for attackers.
When selecting the separate working environment, attention must be paid to appropriate certifications (eg Common Criteria or FIPS 140-2) or quality marks such as "IT Security made in Germany". Also, the hardware of the mobile device should support the necessary security measures itself.

#### SYS.3.2.2.M17 Control of the use of mobile devices (I)

MDM solutions monitor how mobile devices are used. They should be monitored according to several previously defined criteria, for example:

* Up-to-dateness of the operating system of the mobile terminal,
* Up-to-date of installed applications (apps),
* last synchronization with the MDM,
* Adherence to stored data-loss policies,
* Use of cloud services,
Infection with malware, taking into account the operating system of the mobile device and its security frameworks, as well
* Access to the current location.
When monitoring the devices and the user behavior, legal and internal regulations must be observed.

#### SYS.3.2.2.M18 Particularly Secure Operating Systems (CIA)

On the market, there are several providers of particularly secure mobile devices, some of which are certified for the processing of information with high protection requirements or are approved for the processing of secret information (security), so classified as classified information. If there is a high need for protection, the institution should use such a particularly secure mobile terminal and also a corresponding MDM.

#### SYS.3.2.2.M19 Geofencing (CI)

Geofencing is an artificial word from the English words "geographic" and "fence" and refers to the virtual fencing of a geographically clear area. Using MDM systems, geofencing policies allow certain features or apps on mobile devices to be allowed or prohibited only at predefined locations.

For higher protection needs, a protection needs analysis should identify areas where these additional security measures are needed. Subsequently, restrictions should be configured in compliance with legal and internal rules on geofencing policies.

The following examples show application possibilities for geofencing.

**Example 1**

In this example it is assumed that the equipment used is not allowed to leave the premises of the institution. If the devices are outside of a defined range, a warning is sent to the user, to the responsible administrators and to the security management. In order for the user to be able to go back to the permitted area, a time delay should be set before the information is deleted on the device. By actively notifying the security management, the device can detect the security incident and, in the event of a theft, ensure that relevant information does not leave the premises of the institution. It can also use the information to decide if awareness-raising is needed to better address the regulation in the future. Geofencing could also be applied to legal territories to secure information with high protection needs, eg. B. the area of ​​the Federal Data Protection Act or the European data protection area.

** Example 2 **

In a trusted area, the device's automatic lock will not be activated. However, this does not mean that the device is automatically unlocked, only that it will not be locked again after a period of non-use.

** Example 3 **

In a fixed geographic area, the camera of the terminal is disabled or disabled, z. Eg within the company premises or at places with confidential information.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Additional information on threats and security measures in the area of ​​"Mobile Device Management (MDM)" can be found in the following publications, among others:

* #### [BSICS052] Mobile Device Management BSI-CS 052

  

 BSI, Version 1.00, 03.2013
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_052.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_052.pdf)

 
* #### [BYOD] Outline Consumerization and BYOD

  

 BSI, Version 1.2, 07.2013
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Ueberblickspapier\_BYOD\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/ DE / BSI / Grundschutz / download / Ueberblickspapier_BYOD_pdf.pdf)

 
* #### [CC] Common Criteria for Information Technology Security Evaluation (CC)

  

 published in the series of standards ISO 15408: Information technology- Security techniques- Evaluation criteria for IT security, Version 3.1, (last accessed on 28.09.2017)
 <Www.commoncriteriaportal.org>

 
* #### [DIN66399] DIN 66399- Office and data technology - destruction of data media

  

 Beuth Verlag

 
* #### [FIPS1402] FIPS PUB 140-2: Security Requirements for Cryptographic Modules

  

 Federal Information Processing Standard (FIPS) Publication, National Institute of Standards and Technology (NIST), 2001
 <Http://csrc.nist.gov/groups/STM/cmvp/standards.html>

 
* #### [NIST18001D] SECURING ELECTRONIC HEALTH RECORDS ON MOBILE DEVICES

  

 SPECIAL PUBLICATION 1800-1d, NIST, 07.2015
 [https://nccoe.nist.gov/sites/default/files/nccoe/NIST\_SP1800-1d\_Draft\_HIT\_Mobile-StandardsControls.pdf] (https://nccoe.nist.gov/sites/default/ files / nccoe / NIST_SP1800-1d_Draft_HIT_Mobile-StandardsControls.pdf)

 
* #### [NIST800124] Guidelines for Managing the Security of Mobile Devices in the Enterprise

  

 Special Publication 800-124 Revision 1, NIST, 06.2013
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf] (http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf)

 
* #### [TR02102] Cryptographic method recommendations and key lengths

  

 BSI, (last accessed on 27.09.2017)
 [Https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm. html)
