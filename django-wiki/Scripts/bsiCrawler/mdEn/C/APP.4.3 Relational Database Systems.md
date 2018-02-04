Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Database systems (DBS) are a widely-used tool for organizing, creating, modifying, and managing large collections of data. A DBS consists of the so-called database management system (DBMS) and one or more databases. A database is a collection of data together with their description (metadata), which are stored persistently in the database system. Since database systems are of central importance in an IT infrastructure, they result in essential security requirements. In most cases, the core processes of an institution depend on the information from the databases, resulting in corresponding availability requirements. In addition, there are often high demands on the confidentiality and integrity of the information stored in the databases.

### 1.2 Objective

The goal of the module is to be able to operate relational database systems safely and to adequately protect the information that is processed and stored in databases. For this purpose, requirements are described with which database systems can be safely planned, implemented and operated, and which can reduce specific hazards.

### 1.3 Delimitation

This module describes requirements for relational database systems. Security requirements for non-relational database systems are not the subject of this module, but are listed in the module APP.4.5 * Non-relational database systems *.

In order to consistently protect the information in the databases, security requirements should already be taken into account in the development of the database tables and access to the database. However, requirements for this are not listed in this module, but can be found z. In CON.3 * software development *, APP.3.1 * web applications * and APP.3.5 * web services *.

Similarly, the module does not address hazards and requirements that affect the operating system and hardware underlying the database system. Aspects can be found in the corresponding operating system-specific building blocks of the layer IT systems, eg. SYS.1.3 * Unix server * or SYS.1.2.2 * Windows Server 2012 *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in relational database systems:

### 2 1 Insufficient sizing of system resources

If the hardware of a database system does not have enough system resources, there is a risk that the database will fail or malfunction. As a result, for example, data can not be saved. At peak times, resources can also be used to a great extent, thereby impairing performance. This, in turn, may result in applications not running or not performing properly.

### 2 2 Enabled standard user accounts

During the initial installation or in the delivery state of a database management system, user and administration accounts are often not secured or only with passwords that are publicly known. There is a risk that these accounts will be misused. For example, an attacker with the publicly known credentials can log in to the database management system as a user or even as an administrator. Then he can read, manipulate or delete the configuration or the stored data.

### 2 3 Insufficient allocation of authorizations
If authorizations are assigned or managed incorrectly, persons in charge or users of the database management system can receive authorizations that go beyond what is absolutely necessary. Thus, it is possible that the overly entitled persons or users carry out unauthorized actions on the database management system that have far-reaching consequences, as the following example shows:

An incorrect SQL statement (for example, in an installation script) unintentionally deletes a large number of records in the database. Afterwards it is determined that the user actually only needed read-only rights for these data records, but also unnecessarily had delete rights.

### 2 4 Unencrypted database connection

In the default configuration, many database management systems connect to the applications unencrypted. If communication between applications and the database management system is unencrypted, transmitted data and access information can be read or manipulated in transit.

### 2 5 Data loss in the database

Hardware or software failure as well as human error may cause data loss in the database. Since databases usually store important information for applications, services can fail or entire production processes can be shut down.

### 2 6 Loss of integrity of stored data

Incorrectly configured databases, software errors, or manipulated data may violate the integrity of the information in the database. If this is not noticed or noticed late, core processes of the institution can be severely impaired. For example, if the integrity relationships (referential integrity) between the tables are not defined correctly, it may cause the data in the database to be in a bad state. If this error is only noticed during productive operation or not at all, not only the inconsistent data must be laboriously cleaned up and reconstructed. Over time, the extent of damage can also have occurred, for example if critical data (tax-relevant data, billing data or even control data for entire production systems) is concerned.

### 2 7 SQL injections

One common attack on database systems is SQL injection. If an application accesses the data in a SQL database, commands are sent to the DBMS in the form of SQL statements. If input data within the application is insufficiently validated, an attacker can inject their own SQL commands into the application, which are then processed with the authorization of the service account of the application. An attacker could read, manipulate, delete, add new data, or invoke system commands. Although SQL injections primarily affect the applications in the frontend, they have a significant impact on the database system itself and the associated infrastructure.

### 2 8 Insufficient patch management

Due to the extensive range of functions of the database management systems, errors or weaknesses occur relatively frequently, which are remedied by patches and updates by the manufacturer. However, if these are not brought in or are recorded too late, weak points can be exploited and the database management system successfully attacked. This makes it possible for attackers to manipulate the systems to drain business-critical data, shut down services or shut down entire production processes.

### 2 9 Insecure configuration of the database management system
Often, in the default configuration of the database management system, unneeded features are enabled that make it easier for a potential attacker to read or manipulate information from the database. For example, an attacker can connect to an unused programming interface by an unmodified default installation to administer the DBMS without having to authenticate. This allows him to access the databases of the institution without authorization.

### 2 10 malware and insecure database scripts

In many database management systems, it is possible to automate certain actions via scripts executed in the context of the database, e.g. Using the Procedural Language / Structured Query Language (PL / SQL). These include, among others, so-called database triggers. However, if these are used unchecked by those responsible, there is a risk that the database scripts will not meet the requirements of the institution's software development.

Also, an attacker could manipulate core functions (such as Data Dictionary Tables) of a database, such as by using malicious programs or database scripts. This type of attack is difficult to detect. Quality deficiencies in these scripts and malware can compromise the confidentiality as well as the integrity and availability of the data stored in the databases.
