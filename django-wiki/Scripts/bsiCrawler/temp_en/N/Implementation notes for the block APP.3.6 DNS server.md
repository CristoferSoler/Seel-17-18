Table of content

[Toc]

1 description
--------------

### 1.1 Introduction

CHANGED These implementation notes cover the basic security features of the Domain Name System (DNS) and the servers required for this purpose. DNS is a network service that is used to transform host names of IT systems into IP addresses. Normally, a hostname is searched for the corresponding IP address (forward resolution). If, however, the IP address is known and the host name is searched, this is called backward resolution. The term DNS server literally stands for the software used, but is usually also used as a synonym for the computer on which this software is operated.

DNS servers can be distinguished according to their tasks, there are basically two different types: Advertising DNS server and Resolving DNS server. Advertising DNS servers are usually responsible for processing requests from the Internet. Resolving DNS servers, on the other hand, process requests from the internal network.

A failure of a DNS server can seriously affect the operation of an IT infrastructure. It is not directly the failed DNS system problematic, but the resulting restriction of DNS-based services. Under certain circumstances, web servers, e-mail servers are no longer available and the remote maintenance does not work anymore. As DNS is required by many networking applications, the specification (RFC 1034) requires at least two Authoritative DNS servers to operate on each zone.

Since a well-functioning name resolution is a prerequisite for many applications and thus for a smooth operation, DNS servers should be carefully planned, implemented and operated properly. Therefore, the focus of these implementation notes is on the availability of DNS servers and the integrity of the information being transmitted, as well as problems that may arise during DNS server operation.

### 1.2 Life cycle

** planning and conception **

Before a DNS server is selected and the infrastructure is planned, it should be checked whether the desired domain name is still owned by the institution or still available (see APP.3.6.M8 * Domain Name Management) *. If DNS Security Extensions (DNSSEC) are to be used, the measure APP.3.6.M17 * Use of DNSSEC * should be implemented. Planning determines how the DNS servers are integrated into the network infrastructure of the information network (see APP.3.6.M1 * DNS Use Planning *). It should also be decided what the performance capacity of a DNS server must be. On the one hand, this affects the IT system itself and, on the other hand, the transmission capacity of the network connection (see APP.3.6.M11 * Sufficient dimensioning of the DNS server *).

**Procurement**

There are different software products in the field of DNS servers. In order to make an appropriate choice, it must be checked whether the potential products have all the required functions and that all security requirements can be met with them (see APP.3.6.M10 * Selection of a suitable DNS server product *).

**Implementation**

After planning is complete and the software is installed on the server's operating system, the DNS server must be securely set up and configured (see APP.3.6.M4 * Secure Basic Configuration of a DNS Server *, APP.3.6.M6 * Dynamic Backup DNS updates * and APP.3.6.M13 * Limitation of visibility of domain information *). In addition, responsible personnel should be trained to be sufficiently familiar with the security measures that are relevant to them (see APP.3.6.M12 * Training of Responsible Persons *).

**Business**

During operation, it is important to be aware of current security vulnerabilities in order to install any existing software updates or implement other security measures (see APP.3.6.M5 * Timely Import of Security-Related Patches and Updates *). Furthermore, packet filter rules should minimize communication between the DNS server and other DNS servers and clients (see APP.3.6.M16 * Integrating a DNS server into a "P-A-P" structure *). In order to ensure a smooth operation and to detect possible malfunctions or anomalies, it is necessary to continuously monitor the DNS server and to analyze its log data regularly (see APP.3.6.M7 * Monitoring of DNS servers * and APP.3.6.M15 * Evaluation the log data *).

If a DNS server is configured or the DNS information is changed manually, the domain information should be backed up beforehand so that it can be restored if necessary.

** ** segregation

If DNS servers are taken out of service, these should be disposed of in a regulated manner (see APP.3.6.M19 * Separation of DNS servers *).

**
