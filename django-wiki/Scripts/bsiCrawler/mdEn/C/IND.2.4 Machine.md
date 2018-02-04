[toc]
 
1 description
--------------

### 1.1 Introduction

A machine is a technical device that performs automated tasks. A typical example of this is a machine tool that processes products in a predefined manner. It is controlled by an IT system using a program that specifies the appropriate work instructions and steps. Such machines are also referred to as machines.

In most cases, machines are designed by machine builders and equipped with certain predefined functions. However, the operator of the machine can still determine the parameters according to which they should work. For example, molds that are to be milled or calibrations for specific materials can be set. In order for the operator to change the parameters, machines have different interfaces, eg. B. for removable drives, specialized programming devices or network accesses.

Often mechanical engineering also offers remote maintenance services to detect early wear or to react quickly in problem situations.

### 1.2 Objective

The module describes how electronically controlled, semi- or fully automatic machines (eg CNC machines) can be protected independently of manufacturer, type of construction, special purpose and location.

### 1.3 Delimitation

This module supplements the higher-level module IND.2.1 * General * * ICS component * and assumes that this has been implemented. In addition, only requirements are defined for machines whose internal structures an institution can not access.

Also no safety requirements for operating and control technology are described. For this, the block IND.1 * Operating and Control Technology * must be implemented. Similarly, the area of ​​functional safety (safety) is not covered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the machine sector:

### 2 1 Failure or malfunction due to insufficient maintenance

When machines are not regularly maintained, they will not work correctly or shut down completely. Due to malfunction z. For example, employees may be at risk or production may be significantly affected.

### 2 2 Targeted manipulations

If the interfaces of a machine are insufficiently protected, attackers can manipulate the parameters of the machine, eg. Via local programming devices or network services. As a result, workpieces can be damaged or entire product series can be faulty. The attackers can also damage the machine itself, which also causes an economic loss.
