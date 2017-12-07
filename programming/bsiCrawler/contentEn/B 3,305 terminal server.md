#B 3,305 terminal server
## Description 
Terminal servers centrally provide resources that multiple clients can use. These resources can be components of the server operating system, standard applications or command lines. In this way, applications can be deployed without having to be installed on the clients. As a rule, several clients can simultaneously access the applications offered by the terminal server via the network.

Terminal servers represent a particularly centralized scenario of a client-server architecture. Applications are installed on the high-performance terminal servers, which are started, controlled and displayed by the clients. These inputs and outputs can be processed on relatively simply equipped workstation computers (fat clients) with the appropriate client software. There are also solutions that work with dedicated terminals (thin clients).

In this module, a systematic way is shown how to create a concept for the use of terminal servers within an institution and how its implementation and embedding can be ensured. It is applicable to every terminal server of the considered information network.

Demarcation of the module

Part of this component are only the dangers and measures specific to terminal servers. Therefore, the B 3.101 General Server block must also be taken into account. If a stand-alone operating system is executed on the terminal server client and this is not obtained from the server, the block B 3.201 General client is also to be considered. Terminal server services exist for numerous operating systems, for example. Unix or Linux, Microsoft Windows and z / OS. The individual implementations differ greatly in many respects, for example through the

* Use of the used transmission protocol,
* Requirements for the transmission rates of the network,
* Requirements for the speed of the server,
* Use of distributed resources and devices and
* in particular by the different configuration and administration of the operating system operating under this service.


For the security of a terminal server, it is therefore essential to additionally use the building blocks that describe the concrete operating system.



## Countermeasures 
In order to safeguard the considered information network, further modules must be implemented in addition to this module, according to the results of the modeling according to IT-Grundschutz.

For the successful development of a terminal server, a series of measures have to be implemented, beginning with the conception over the procurement up to the operation of this server. The steps to be taken and the actions to be followed in each step are listed below.



###Planning and conception
When planning a terminal server, a number of basic conditions must be considered. In the first step, the general security policy should be supplemented by a detailed directive for terminal servers (see M 2.464 Creating a security policy for terminal server usage). The specifications and objectives set forth herein must reflect the individual conditions and requirements of a secure terminal server environment. When migrating an existing client-server architecture to a terminal server-supported environment, it must first be checked in advance whether the applications to be migrated are suitable for this purpose (M 2.466 migration to a terminal server). Architecture).

Within multi-user environments, such as terminal server systems, the separation of users from each other and against risky system functions is of considerable importance. In order to ensure trouble-free operation and to protect the confidentiality of the data processed within individual user sessions, the rights must be granted restrictively (see M 5.163 Restrictive rights assignment on terminal servers).

Terminal servers can be used to allow clients to access content in insecure networks, such as active content websites. Instead of the client, the terminal server communicates via the insecure network, only the content is transmitted to the client. A terminal server that accesses the insecure network instead of the client is called a graphical firewall (see measure M 4.365 Using a terminal server as a graphical firewall).



###procurement
If applications that are currently used in a client-server-based network architecture are to be centrally provided on a terminal server, licensing-relevant contracts must be checked in advance of the migration and possibly procure new software (see M 2.468 Licensing of Software in terminal server environments).



###implementation
The administration of the terminal server infrastructure is in some cases necessary for administrators as well as for users without previous experience. All persons working with a terminal server system should therefore be trained (see M 3.81 Safe Terminal Server Training).



###business
It must be prevented that the users can change the user environment on the terminal servers and only access resources that they should access (see M 4.367 Secure use of client applications for terminal servers). If the connection between terminal servers and their clients is made via an insecure network, precautions must be taken so that the communication can not be overheard, modified or disturbed (see M 5.164 Secure Use of a Terminal Server from a Remote Network). ,



###segregation
If terminal servers, clients connected to terminal servers or infrastructure components of a terminal server environment are to be taken out of operation, the option M .2.469 Controlled shutdown of components of a terminal server environment should be taken into account.



###emergency preparedness
Since the failure of a terminal server environment can usually affect a larger number of users, measures must be taken to reduce the damage in the event of a failure. Terminal server connections can also meet high availability requirements (see M 6.142 Use of redundant terminal servers).

If a terminal server client fails, the applications on the terminal server are no longer available to the affected user. Therefore, replacement machines without terminal operating systems (thin clients) could be kept available (M 6.143 Deployment of terminal server clients from depot maintenance).

If, as a precautionary measure, the applications are installed both on the terminal server and on the client PCs, an emergency operation can be temporarily maintained in the event of a failure (M 6.144 Configuration of terminal server clients for dual use as normal client PCs) ,

The following is a description of the set of measures for the Terminal Server block.



