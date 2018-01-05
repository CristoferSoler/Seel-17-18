1 description
--------------

### 1.1 Introduction

A machine is a technical device that performs automated tasks. A typical example of this is a machine tool that processes products in a predefined manner. It is controlled by an IT system using a program that specifies the appropriate work instructions and steps. Such machines are also referred to as machines.

In most cases, machines are designed by machine builders and equipped with certain predefined functions. However, the operator of the machine can still determine the parameters according to which they should work. For example, molds that are to be milled or calibrations for specific materials can be set. In order for the operator to change the parameters, machines have different interfaces, eg. B. for removable drives, specialized programming devices or network accesses.

Often mechanical engineering also offers remote maintenance services to detect early wear or to react quickly in problem situations.

### 1.2 Objective

The module describes how electronically controlled, semi- or fully automatic machines (eg CNC machines) can be protected independently of manufacturer, design, special purpose and location.

### 1.3 Delimitation

This module supplements the higher-level module IND.2.1 * General * * ICS component * and assumes that this has been implemented. In addition, only requirements are defined for machines whose internal structures an institution can not access.

Also no safety requirements for operating and control technology are described. For this, the block IND.1 * Operating and Control Technology * must be implemented. Similarly, the area of ​​functional safety (safety) is not covered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the machine sector:

### 2 1 Failure or malfunction due to insufficient maintenance

If machines are not regularly maintained, they will not work correctly or shut down completely. Due to malfunction z. For example, employees may be at risk or production may be significantly affected.

### 2 2 Targeted manipulations

If the interfaces of a machine are insufficiently protected, attackers can manipulate the parameters of the machine, eg. Via local programming devices or network services. As a result, workpieces can be damaged or entire product series can be faulty. The attackers can also damage the machine itself, which also causes an economic loss.

3 requirements
---------------

The following are specific requirements for the machine area. Basically, the ICS Information Security Officer (ICS-ISB) is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the defined security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### IND.2.4.A1 Remote Maintenance by Machine and Plant Builder [ICS Administrator]

For the remote maintenance of a machine SHOULD there be a central guideline. In it SHOULD be regulated how the respective remote maintenance solutions are to be used and how communication links are protected. It SHOULD also describe what activities should be monitored during remote maintenance.
In addition, it should NOT be possible to remotely access a machine to other systems or machines of the institution.

It should be agreed with a service provider how to use the information stored in the machine.

#### IND.2.4.A2 Post-warranty Operation [ICS Administrator]

A process SHOULD be established to ensure that the machine can continue to operate safely beyond the warranty period. For this purpose, further support services should be contractually agreed with the supplier.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of machines. They SHOULD be implemented in principle.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

4 Further Information
------------------------------

### 4.1 Literature

Further information about hazards and safety measures in the area "Machine" can be found in the following publications:

5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the "machine" block.

* G 0.11 Failure or disruption of service providers
* G 0.14 Spying out information (spying)
* G 0.18 Missing planning or missing adjustment
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.39 Malware
The cross reference tables can be found in the download area due to their size.
