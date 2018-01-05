1 description
--------------

### 1.1 Introduction

In this module, devices with functions from the field of Internet of Things (IoT) are considered. In contrast to "classic" IT systems, these are "intelligent" objects that contain additional "smart" functions. IoT devices are typically connected to data networks, in many cases wirelessly, and can often access and be accessed over the Internet. This can have an impact on the information security of the entire information network.

IoT devices can be present in institutions because they are brought by employees or external, for. For example, smartwatches or wearables. In many institutions but also IoT devices are procured and operated, z. For example, devices such as fire, gas, and other alarms, coffee machines, or building control elements such as cameras and HVAC (Heating, Ventilation, and Air Conditioning).

In general, a distinction can be made between directly addressable IoT devices and IoT devices that require a central control unit. Directly addressable devices are usually connected to a data network with their own IP address and can act autonomously or managed by a central control unit. But there are also IoT devices that only communicate directly with control units, eg. B. over wireless networks such as Bluetooth or ZigBee, and thus not directly connected to data networks. The range of these radio links can, if provided, be increased by a separate, meshed network, with each device establishing a radio link with each device.

### 1.2 Life cycle

** planning and conception **

In the planning and design phase, the use of IoT devices within the institution should be defined. In this case, the use of IoT devices must be carefully documented and planned (see * SYS.4.4.M6 Inclusion of IoT Devices in the Security Policy of the Institution * and * SYS.4.4.M7 Planning of the Use of IoT Devices *).

**Procurement**

In order to be able to select suitable IoT devices for the institution, the devices must comply with this with regard to the security criteria, eg. For example, update functions, update process or authentication variants can be viewed (see * SYS.4.4.M1 Application Criteria for IoT Devices *). Other criteria, such. Eg organizational constraints or material safety should also be taken into account (see * SYS.4.4.M8 procurement criteria for IoT devices). *

**Implementation **

After planning and procurement have been completed, the devices must be installed and configured based on security requirements. Before the IoT devices are installed, the operating environment and power supply should be checked to ensure the safe operation of the devices (see * SYS.4.4.M21 Operating Environment and Power Supply). * During installation, various adjustment options should be considered and implemented, such as: , For example, to control and secure access to the devices (see * SYS.4.4.M10 Secure Installation and Configuration of IoT Devices). *

**Business**

Before IoT devices are put into operation, their use should be approved by examining the installation and configuration documentation. During operation, in addition to the logging of important and safety-relevant events, it is also important to monitor the network traffic of the IoT devices (see * SYS.4.4.M17 Monitoring the network traffic of IoT devices * and * SYS.4.4.M18 Logging of safety-relevant events IoT devices *).

** Separation **

When IoT devices are discarded, it should be ensured that no important or sensitive data remains on the IoT devices (S * YS.4.4.M20 Regulated decommissioning of IoT devices *).

2 measures
-----------

The following are specific implementation notes in the "General IoT Device" section.

### 2.1 Basic measures
The following measures should be implemented as a priority:

#### SYS.4.4.M1 Usage criteria for IoT devices

Many existing on the market IoT devices have little to no security mechanisms and some contain various vulnerabilities. For IoT devices to be deployed in institutions, they must meet a minimum of security criteria.

The devices must have update functions and the manufacturer must offer an update process. If IoT solutions have insufficient or missing patch management, no vulnerabilities can be resolved. Alternatively, the security holes would have to be shielded elsewhere. This can be very costly and even the whole concept of use of an IoT device ad absurdum lead.

Another big problem with IoT devices are default and sometimes even hard-coded standard passwords. Devices that can not be authenticated or that can not change default passwords must not be used.

If it turns out during operation that access data are permanently coded in a device, it must be disconnected from the network. This also applies if accessibility possibilities with potential for abuse become known later, such as additional interfaces for remote access (such as Telnet) or master passwords of the manufacturer, and these can not be reliably switched off or prevented.

#### SYS.4.4.M2 Authentication

Companies and authorities should only use IoT devices that enable authentication. This must be activated. If passwords are used, secure passwords must be used. There should be a password policy for this (see also ORP.4 Identity and Permission Management). Basically, the chosen passwords must be complex enough, kept secret and changed regularly. Preset passwords must be changed at start-up, if possible, before a device goes online. In addition, the use of alternative authentication mechanisms, such as. B. Certificate-based authentication. Unfortunately, not all IoT devices offer the same possibilities.

#### SYS.4.4.M3 Regular update

During operation of the IoT devices, it is necessary to regularly check whether new updates / patches are available for the IoT devices used and related components such as sensors or management systems, eg. B. on relevant websites with safety information or the manufacturer. Existing patches and updates must be installed in a timely manner or other security measures must be taken if no patches are available. In the extreme case, the devices may no longer be operated with known, unrecoverable weak points. In addition to the firmware of the IoT devices, third-party components, such as B. administration or management software, be checked for currency. If new updates are available, they must be updated in a timely manner. In general, it must be ensured that patches and updates are only obtained from trustworthy sources, primarily the respective manufacturer itself.

#### SYS.4.4.M4 Enable auto-update mechanisms

Automatic update mechanisms (autoupdate) ensure that the software is updated regularly on the IoT devices. However, in critical environments or high availability requirements, priority should be given to the feasibility of manual maintenance, as automatic, untested updates can cause unexpected effects or even failures.
Even with automatic updates, it is important that they are obtained from trustworthy sources and that the download is suitably secured, for example by appropriate authentication and transport encryption (eg HTTPS). It must not be possible for an attacker to gain access to the IoT devices by misusing updates (such as man-in-the-middle attacks).

#### SYS.4.4.M5 Restricting network access

In order to minimize the network access of the IoT devices, only previously defined incoming and outgoing connections should be allowed by means of a firewall. Overall, outbound connections are to be minimized, both in the internal network and the Internet.

For outgoing connections, the valid destinations of a connection, such as For example, the manufacturer's update server, location of video data, and management system can be configured. If and how IoT devices need to contact the manufacturer's servers to verify the availability of updates should be researched in the product documentation.

Should it be necessary to access the IoT devices from the outside (that is, from the Internet), this should only be done with sufficient authentication.

The release of externally incoming connections in the router should be avoided. When commissioning IoT devices, make sure the UPnP feature is disabled on all routers.

At the perimeter (router, firewall) the access via telnet (port 23) must not be released from outside.

At the perimeter, access via SSH (port 22) may only be released if it is protected with sufficiently secure individual passwords. Higher security is achieved if the access is not secured by username and password but by a software certificate. Again, not one of the standard ports (22, 1022, 2222) should be used, but a random value in the range 10000 to 65535.

If necessary, access can be further secured through the use of VPN. When using VPN, make sure to use strong enough cryptographic procedures and key lengths.

It is also advisable to operate the IoT devices in a separate physical network area or within a separate Virtual Local Area Network (VLANs) to prevent lateral propagation when the IoT devices are compromised.

Based on a well-maintained asset management system, the following measures can prevent unwanted communication:

* Traffic control at gateways, z. For example, through policies on firewalls and access control lists (ACLs) on routers
* Restrictive configuration of routing on IoT devices and sensors, especially the suppression of default routes
* Signatures on Intrusion Prevention Systems (IPS)
* Summary of IoT devices and sensors in its own network segment, which may only communicate with the network segment for management
* Configure Virtual Private Networks (VPNs) between the IoT devices and sensor networks and the management networks
* Disable the UPnP feature on all routers
Depending on the location of the IoT devices, physical access protection should be implemented. This not only protects against vandalism, but also against a change in the configuration, which is often made possible by the factory reset.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "general IoT device".

#### SYS.4.4.M6 Inclusion of IoT devices in the security policy of the institution
The security requirements for IoT devices result from the institution-wide security policy. Based on the general guideline, the requirements for the given context must be specified and summarized in a security guideline for the respective group of IoT devices. In this context, it has to be examined whether, in addition to the institution-wide security guideline, further superordinate requirements such as IT guidelines, password guidelines or Internet usage guidelines must be taken into account.

The security policy must be known to all professionals and other persons involved in the procurement and operation of the IoT devices and should be the basis for their work. As with all directives, their content and implementation must be regularly reviewed by a higher level audit.

The security policy should specify the level of security generally to be achieved and make basic determinations. In order to improve the clarity, it may be useful to develop separate security guidelines for different fields of application.

When creating a security policy, it is recommended to proceed in such a way that first of all a maximum of requirements and specifications for the safety of the IoT devices is established. These can then be adapted to the actual circumstances. Ideally, this will ensure that all necessary aspects are taken into account. The reason for non-consideration should be documented for each deficient or weakened default in the second step. As the security policy for IoT devices is being formulated, it is also important to strike a balance between security and functionality.

#### SYS.4.4.M7 Planning the use of IoT devices

A fundamental requirement for IoT equipment to operate safely is an adequate level of planning in advance. Planning does not only cover aspects that are classically associated with the term information security, but also aspects of physical, physical and functional security, as well as normal operational aspects that impose security requirements.

In a rough concept, for example, the following typical questions should be dealt with:

* What tasks should the IoT devices perform? Which services must be accessible from the IoT devices? Are there any special requirements for the availability of the IoT devices or the confidentiality or integrity of the stored or processed data?
* Which requirements for the IoT devices arise from the general requirements?
It is recommended that you create one or more generic requirement profiles (for example, General IoT Devices, Cameras, or IoT Building Control Devices) that can be used as the basis for concrete planning.

The following subconcepts should be considered in the planning:

* Authentication: Which type of user authentication should be used? Is it necessary to set up users?
* Administration: How should the IoT devices be administered? Are all settings made locally or should the IoT devices be integrated into a central administration and configuration management?
* Network services and network connection: The network connection of the IoT devices should be planned. Above all, the necessary restrictions and monitoring measures should be planned here.
* Logging: Logging also plays an important role in IoT devices, for example, in diagnosing and repairing malfunctions or in detecting and resolving attacks. It makes sense to specify in the planning phase how and at what times log data should be evaluated.
All decisions made in the planning phase must be documented in such a way that they can be reconstructed at a later date. It should be noted that usually other persons besides the author must evaluate this information. Therefore, attention must be paid to appropriate structuring and comprehensibility.

#### SYS.4.4.M8 IoT Device Procurement Criteria [Information Security Officer (ISB), Procurement Agent]

Even when choosing a product, not only the price-performance ratio should be considered, but also aspects of information security. Here above all the offered functionality of the product and the support of the manufacturer play an important role. The ISB should also be involved in procuring equipment that does not have obvious IT functionality in order to assess whether it needs to be integrated into the institution's security design.

Basically, the use of IoT devices with a cloud concept is not recommended. In this case, sensitive data flows via third parties (eg camera manufacturers) and is stored there for access via the Internet. The use of WLAN - especially in critical applications - should be avoided, as far as the conditions of use allow.

A fundamental goal for the safe use of IoT devices is the minimization of the attack surface. In order to keep these low from the outset, it is recommended to procure IoT devices on which only the services / ports required for the specific application are available. Alternatively, it should be possible to disable unnecessary services. If this is also not possible, appropriate restrictions must be made during commissioning at network level (eg firewall) in order to prevent the use of unnecessary services.

To ensure confidential transmission of user and configuration data, the IoT device should support an encryption-based protocol, such as SSL / TLS or SSH. If the product itself does not provide any encryption, this must be ensured during commissioning, eg during the commissioning phase. B. over a Virtual Private Network (VPN), flanking be implemented.

If the application requires it, the IoT devices should provide a differentiated role / rights concept for different users.

Furthermore, the manufacturer must ensure the provision of patches or updates for a sufficiently long period of time. This is usually described with End Of Service (EOS) - not to be confused with End Of Life (EOL), which refers to the end of the production and sale of a product.

IoT devices are often procured in conjunction with higher-level systems, e.g. Building control systems. Together with the pure hardware and firmware, additional components and services can be procured.

If errors are made in the procurement of IoT devices, this can have negative consequences for the secure operation of the higher-level system or even of the entire information network. Before an IoT device is procured, therefore, a list of requirements must be created, by means of which the devices in question are evaluated. Based on the assessment, an informed purchase decision can then be made to ensure that the IoT device meets the safety requirements in practical operation. The list of requirements should essentially comprise the safety-relevant areas and criteria presented below.

** Organizational constraints **

The following aspects should be considered in procurement:

* Can an effective process for supplying security-relevant firmware or software updates be established?
* Does the manufacturer notify the affected departments when security holes become known?
* Does the manufacturer provide technical support who is able to provide information or correct malfunction within a reasonable time?
* Does the manufacturer offer training or manuals for the safety of IoT devices?
** Specifications from the field of application **

The IoT device must comply with applicable standards and standards in the relevant field of application and, if applicable, meet the criteria for a product-specific approval. Such approvals are z. B. in the areas of aviation, road transport and medical technology.

** Material security **

When used in harsh environmental conditions such as humidity, extreme temperatures, mechanical stress and dust, the IoT device must be physically robust. There should be no or few reliable plug connections. Sensitive components should be specially encapsulated and equipped with damping devices. Components with moving components should be avoided as much as possible.

** Failure and operational safety **

Depending on the required availability, requirements for reliability, electromagnetic compatibility, internal monitoring and self-test mechanisms and restart must be set for the IoT device.

** ** System Architecture

The bandwidth for system architectures is very large. In addition to new developments, unlike in the PC or server area, often older architectures and operating systems are used. The reasons for this are the lower cost of the processor itself and the ability to reuse the application design, code and development tools as well as debugging tools. It must be ensured that the chosen system architecture is suitable for implementing the necessary safety functions.

** Operating system and application software **

If the IoT device is procured together with an operating system and / or application software, it must be determined which safety-relevant features they should have, for. As regards

* Use of secure communication protocols
* Safe installation and upgrade
* Security of access and access
* User and rights management
* Logging
* Alerting
* Integrity protection
#### SYS.4.4.M9 Control of the use of IoT devices

Even during operation, there are a number of security requirements for the use of IoT devices. They must be adequately integrated into the technical and organizational environment in which they are used. For this, the following organizational regulations must be made.

It is important to identify those responsible for the operation of the IoT devices, such as updates, maintenance and repair, log analysis, and reaction to security incidents and malfunction. In the event of failures, malfunctions and security incidents, it must be clearly defined what needs to be done.

Regulations must be established to test the safety and functionality of IoT devices. The requirements for the physical environment of use, such. As the humidity and temperature range and the power supply must be specified. If necessary, additional infrastructure measures should be established.

The IoT devices should be configured so that adequate security and functionality can be achieved. The configuration of the IoT devices must be documented so that they can be refurbished after replacement, updating, or rebuilding a system according to security requirements.

#### SYS.4.4.M10 Secure installation and configuration of IoT devices

After you finish planning new IoT devices and creating a security policy, you can start installing the IoT devices.
The installation and configuration of the IoT devices should only be performed by authorized persons (responsible for IoT devices, administrators or contracted service providers). Administrators for IoT devices and their representatives must be carefully selected. You must be regularly informed that the powers may be used only for the required administrative tasks. Since administrators have a key role to play in the functionality of the hardware and software used, the continuation of activities must be ensured even if administrators fail. For this, the named representatives must have the current state of the system configuration and have access to the passwords, keys and security tokens required for the administration.

**Installation**

During installation and later configuration, at least the important steps should be documented so that they can be understood at a later time. For example, a checklist can be created for the installation, where the steps taken can be ticked off and the settings made can be noted. A corresponding documentation is helpful for an error analysis or later reinstallation. It should be noted that, in addition to the author, other administrators, who may be less specialized in this field, have to resort to the documentation. Therefore, it is important that the documentation is well structured and understandable.

It should be avoided that other IT systems can access the IoT device to be installed during installation. This is important because during the installation usually no passwords are assigned and no protection mechanisms are active, but possibly already accesses are possible. If the installation of the IoT devices should or must be done over the network (for example, reloading of packages), it is recommended to use an installation server in the secure administration network.

If this has not already been done automatically, logging of the system events should be activated at the latest when completing the basic installation. The log data can provide valuable information in case of problems during further installation and configuration.

**Configuration**

The basic settings made by the manufacturer or distributor of an IoT device are usually not optimized for security, but rather for ease of installation and commissioning, as well as often allowing each user to easily access as many features of the IoT device as possible. When using IoT devices in government agencies or companies, this is often undesirable.

The first step in the basic configuration must therefore be to check the basic settings and, if necessary, to adapt them to the specifications of the security policy. The basic configuration is of course relatively heavily dependent on the operating system used. For this reason, the operating system-specific components contain corresponding, more detailed recommendations.

Goals of a secure basic configuration should be that

* the IoT devices are protected against "simple" attacks over the network,
* no one can obtain access to sensitive data that is not intended for him, purely by curiosity or even accidentally
* No one can cause serious damage to the IoT devices when working with the IoT devices due to pure operator errors; and that
* the impact of minor errors is limited as much as possible.
The settings that should be checked and adjusted as part of the basic configuration concern in particular the following areas:

** Settings for System Administrators **
Not all IoT devices offer a dedicated rights and role model. If so, the identifiers under which system administrators work should be particularly secure. These settings should be checked and adjusted if necessary.

** Settings for user IDs and user directories **

As part of the basic configuration, it should be checked which standard settings apply to user IDs. The settings may need to be adjusted according to the security policy. This essentially applies to the same parameters as system administrator identifiers, but other users may want to make other settings useful.

** Settings for access to the network **

As part of the basic configuration, the settings for access to the network and important external services should also be taken and documented.

** Deactivation of "Call Home" functions **

Some IoT devices send information, such as about errors that have occurred or about the system configuration, directly to the manufacturer, so that he can adapt the product to the needs of the user in the future. For this purpose, a data connection is established via data networks, such as the Internet, to the servers of the manufacturer. Such a form of data leakage can be critical, especially if users are not informed about the frequency and content of the data transfer.

In general, this often unwanted exchange of information should be prevented. If and how information is sent can usually be found in the license agreements of the software used.

Many applications offer the possibility to deactivate this "Call Home" function. Only in justified exceptional cases, this should remain activated. After updates it should be checked if the "Call Home" function is still disabled.

Local packet filters or the central security gateway (firewall) can also be used to prevent the establishment of a connection with the manufacturer. For example, based on the destination addresses or port numbers, the data connections could be rejected. It should be noted that the consideration of all applications is complex and automatic update functions, if needed, are then often no longer available.

#### SYS.4.4.M11 Using secure protocols

Care should be taken to ensure that IoT devices already support an encryption-based protocol (eg SSL / TLS or SSH) when purchasing (see SYS.4.4.A8 procurement criteria for IoT devices). During commissioning, care must be taken to activate existing secure protocols and deactivate any insecure ones (such as telnet). If the product itself does not provide any encryption, this must be ensured during commissioning, eg during the commissioning phase. B. over a Virtual Private Network (VPN), flanking be implemented.

As far as possible, all unnecessary network protocols should be deactivated on the IoT devices (see SYS.4.4.M13 Deactivation and uninstallation of unneeded components).

#### SYS.4.4.M12 Secure integration into higher-level systems [Information Security Officer (ISB)]

IoT devices are often used in conjunction with higher-level management systems, e.g. Building control systems.

IoT devices such as surveillance cameras, room and environment sensors should only communicate with the associated management system. Communication of these systems with the Internet is usually not necessary and should be prevented.

#### SYS.4.4.M13 Disabling and uninstalling unneeded components
Often, after a standard installation of an IoT device, a larger number of user IDs, protocols, services, functions, interfaces, and other components are set up that are not always necessary for operation, and therefore may be a source of security vulnerabilities. This applies in particular to network services. Therefore, it should be checked in the basic configuration, which protocols and services are really needed. Unnecessary services of the IoT devices should be deactivated or completely uninstalled. This is especially true for chronically insecure services such. Telnet or SNMPv1 / v2.

Unnecessary user IDs should either be deleted or at least deactivated in such a way that it is not possible to log in to the IoT device under the ID in question.

Some interfaces may present potential security issues that must be addressed through appropriate organizational or technical security measures. Interfaces whose use should be controlled include Bluetooth, Wi-Fi, Zigbee, Firewire, eSATA (external SATA HDD connection) and Thunderbolt. The use of unnecessary interfaces should be prevented. On many devices, the radio interfaces can not be deactivated, then the use of the devices must be checked (protection requirements, control and restriction options against each other).

The check for running services should be done externally by a port scan from another system.

#### SYS.4.4.M14 deployment clearance

Before IoT devices are used in productive operation and before they are connected to a productive network, the application should be released. This must be documented. The deployment clearance is based on a test of the installation and configuration documentation and the functionality of the IoT devices in a test. It is carried out by a body authorized to do so in the institution. More detailed information can be found in OPS.1.1.7 Software Testing and Approvals.

#### SYS.4.4.M15 Restrictive rights assignment

In principle, authorizations should always be restrictive so that users can access exactly the services and data they need for their tasks.

#### SYS.4.4.M16 Eliminate malware on IoT devices

Depending on the type and area of ​​application of IoT devices, these can be infected by malicious programs. How infections can be prevented and how they can be eliminated depends on the operating systems used. This should be updated regularly with the latest safety information.

Current malicious software on surveillance cameras and other IoT devices is often only in volatile memory, rather than persistent in the system einzunisten. Therefore, a regular restart of such IoT devices is advisable. This can clear an infection, although it does not protect against reinfection.

If the cause of the infection can not be remedied or a new infection can be effectively prevented, the affected IoT devices should no longer be used.

#### SYS.4.4.M17 Monitoring the network traffic of IoT devices

It is advisable to regularly check the communication (incoming and outgoing connections) for abnormalities. Firewalls log files can provide accurate information about who the IoT devices want to communicate with about which service and whether these connections were allowed or blocked. Furthermore, the IoT devices or the associated administration or management software can provide information as to whether the IoT devices are expected to be used.

If preventive suppression of unwanted communication is not possible, the following measures can help with detection:

* Activation and, if possible, centralized collection and evaluation of log data of systems and components.
* Automatic filters on these log data that trigger an alarm when network traffic is being monitored by the IoT devices or sensor systems to non-management systems.
* Analysis of network statistics e.g. with Netflow.
#### SYS.4.4.M18 Logging of security-related events on IoT devices

In principle, safety-relevant events must be logged during the operation of IoT devices. The technical possibilities for this can vary greatly with different types of IoT devices and their environment. Possible characteristics, functionalities and parameters are:

* Logging into a non-volatile memory, cumulative by different processes,
* Data recording in simple, formatted text files, CSV or
* Recording of process data via datalogger, in time, event-driven or with changes,
* Structured storage of events in a database system,
* Real-time monitoring with information from a user and the possibility of interaction at runtime,
* Logging of all or configurable state and transition changes,
* Variable Tracing, Audit Trails,
* Statistical evaluation in report form or as graphical representation and
* Correlation, rating.
As far as possible, IoT devices should at least record security breaches, such as attempted and enforced unauthorized access and access. In particular, the activities of privileged users should be monitored, such as technicians and administrators. Although this can not prevent the misuse of rights, it is the prerequisite for deliberately closing vulnerabilities.

If electronic logging is not or only partially feasible due to technical limitations due to the limited resources, organizational regulations should be created. On the one hand, all work on an IoT device with details of place, time, performer and type and cause of activity should be recorded in a logbook. On the other hand, all failures, obvious access and access violations and other abnormalities should be documented in the logbook. The entries should be evaluated regularly and according to the occasion.

Both automatically generated logs and records by personnel must be protected against unauthorized subsequent changes. Only dedicated users can access the logs. As far as technically possible, precautions must be taken that the log data can not be deleted or changed by privileged users, by storage on non-rewritable data carriers or by means of electronic signature. Data carriers with log data must be stored securely and the persons involved must be instructed in the correct handling.

#### SYS.4.4.M19 Protection of the administration interfaces

Depending on whether IoT devices

* locally, ie on the device itself, directly via the network, ie on another IT system via a corresponding web interface provided by the IoT device itself, or via central network-based tools, ie via a management software on a server,
* directly via the network, ie at another IT system via a corresponding web interface provided by the IoT device itself, or via central network-based tools, ie via a management software on a server,
* via central network-based tools, ie via a management software on a server,
appropriate security precautions should be taken. The methods used for administration should be specified in the security policy and the agreed security arrangements briefly described. The security policy also specifies how to administer the IoT devices. For administration over the network, secure protocols should be used.

#### SYS.4.4.M20 Regulated decommissioning of IoT devices
When decommissioning IoT equipment, make sure that

* no important data that may be stored on it is lost, and that
* no sensitive data remains on the media of IoT devices.
In particular, it is important to have an overview of what data is stored on IoT devices.

* Dismiss the IT system from directory services and databases
 Any permissions on the network that are paired to an IoT device must be deleted. Examples include entries on proxy servers on the security gateway or access rights to network services that are granted based on the IP address. If an IoT device is entered in network-wide directory services or databases, the associated entries must be deleted or at least the corresponding identifiers must be deactivated.
* Delete the data on the IoT devices
 It must be ensured that no more valuable information is present on the storage areas of IoT devices. All data stored or permanently stored on data carriers should be deleted in such a way that they can not subsequently be readably restored and misused by special software. If it is not possible to delete the data securely, the data carriers concerned should be destroyed if the protection requirements are higher.
* Remove any other information
 If an IoT device still stores sensitive data in other locations, for example in a non-volatile memory or in the cloud, then these must also be deleted when the device is decommissioned.
### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### SYS.4.4.M21 Operating environment and power supply [Information Security Officer (ISB), Building Services] (I)

Before IoT devices are installed, it should be clarified whether they may be operated in the envisaged operating environment. For example, the ISB should consider whether IoT devices, such as cameras, are useful for viewing input devices (keyboards, PIN pads) or monitors. These could thus also record confidential access data. Depending on the protection requirements of the environment, potentially unsafe devices should not be installed at all. IoT devices such as cameras must also comply with the relevant privacy policies.

It should be clarified whether an IoT device has specific requirements for the physical environment of use, such as: As humidity, temperature or energy supply. This is especially important for outdoor IoT devices. If necessary, supplementary infrastructure measures should be implemented, such as suitable containment.

IoT devices should be protected from theft, destruction and tampering in the environment of use. This can be achieved for example by suitable attachment or additional protection mechanisms such as enclosures. This is especially important when attached to the external peripherals devices such. B. for video surveillance.

IoT devices are often not connected to power grids, but are powered by batteries. Then the regular function test and replacement of the batteries should be regulated.

IoT devices should be protected against dust and dirt according to their intended use and intended location.

#### SYS.4.4.M22 System Monitoring (A)
In order to be able to react to critical system events, a suitable system monitoring or monitoring concept should also be created for IoT devices. This includes the continuous monitoring of the system status and functionality of the IoT devices. If errors occur or defined limit values ​​are exceeded or undershot, this should be reported automatically to the operating personnel. For this, the IoT devices should be integrated into a suitable system monitoring or monitoring concept.

#### SYS.4.4.M23 Auditing IoT Devices (CIA)

All IoT devices should be checked periodically to ensure that they are configured correctly and that all specified security measures have been implemented. If deviations from the target state are found and remedial measures are known, these should be documented.

In addition, at least in safety-critical areas, all IoT devices to be used should be checked by experts before use for safety reasons.

#### SYS.4.4.M24 Secure Configuration and Use of an Embedded Web Server (CIA)

Some IoT devices have an integrated web server that can be used to retrieve and control information. This is usually a so-called Embedded Web server with limited functionality, which is optimized for the most scarce resources. There are many embedded web servers available on the market, they are small in size, have a moderate CPU load and are largely platform-independent. The main task is to transfer web documents to the client via HTTP (S). Some also master the dynamic creation of documents, such as server-side scripting.

For an embedded web server, only the required components and functions should be installed or activated if possible. Some IoT devices have few or no configuration options. The web server should run under an account with the least possible rights. If higher privileges are required to start, then you should switch to a non-privileged account. All messages relevant to security and error handling should be logged, eg. For example, it structures for successful and unsuccessful accesses, internal errors, incorrect or incomplete HTTP requests, and other relevant system messages. This logging should be described in the security documentation (further information can be found in OPS.1.1.6 logging). The web server should only communicate via a secured SSL connection if possible and access should only be possible after strong authentication.

3 Further information
------------------------------

### 3.1 Worth knowing

There are also security measures that could be implemented to secure IoT devices and that are useful depending on the environment and protection needs. This includes:

* Penetration tests or security analyzes of the IoT devices or their firmware
* Check for hidden links (especially in the area of ​​administration functions)
* Addition of missing or insufficient authentication functions
* Available features at the console level
This is the area where further safety considerations and measures can be collected and complementary measures derived. Please send your ideas to us.

### 3.2 Literature

More detailed information on hazards and safety measures in the area of ​​"general IoT device" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ACS1] Security of IP-based surveillance cameras

  

 CSE 128, Version 1.0, Alliance for Cyber ​​Security, 11.2016
[https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_128.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/downloads/BSI-CS_128.html)

 
* #### [ACS2] Espionage attacks using backdoors in security cameras and room sensors

  

 How To Protect Your Business, Expert Group Cyber ​​Security, Alliance for Cyber ​​Security, 10-2016
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161010\_expkr\_statement01.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE /_/partner/161010_expkr_statement01.pdf)

 
* #### [DHS] Department of Homeland Security

  

 Securing the Internet of Things, 12.2016,
 <Https://www.dhs.gov/securingtheIoT>

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (last accessed on 28.09.2017)
 <Https://www.owasp.org>
