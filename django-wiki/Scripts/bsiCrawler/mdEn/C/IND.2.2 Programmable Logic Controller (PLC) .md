Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

A Programmable Logic Controller (PLC) is an ICS component. It handles control and regulating tasks in operational technology (English: Operational Technology, OT). The boundaries between different device classes and designs are today fluent: For example, even a remote terminal unit (RTU) can take over the functions of a PLC or a Programmable Automation Controller (PAC) can try the advantages of a PLC and an industry To unite -PCs. However, the PLC is still the classic automation device, so in this module these terms are used synonymously.

A PLC has digital inputs and outputs, a real-time operating system (firmware) and other interfaces for Ethernet or fieldbuses. The connection to sensors and actuators takes place via the analog or digital inputs or outputs or via a fieldbus. Communication with process control systems usually takes place via the Ethernet interface and IP-based networks.

The possible implementations are manifold: PLCs can be used as a module, as a single unit, as a PC plug-in card (slot PLC) or as software emulation (soft PLC). The most common are modular PLCs, which are composed of different functional plug-in modules. Increasingly, other functions such as visualization, alarming and logging are realized by the PLC.

Due to the high availability requirements typical in the OT environment and the often extreme environmental conditions (climate, dust, vibration, corrosion), ICS components have always been designed as robust devices with high reliability and a long service life.

PLCs are usually configured or programmed using special software from the respective manufacturer. This is done either via so-called programming devices (eg as an application under Windows or Linux) or via an engineering station that distributes the data over a network.

### 1.2 Objective

The aim of the device is to protect all types of programmable logic controllers, regardless of manufacturer, type, purpose and location. It can be applied to a single PLC or a contiguous board used as a PLC.

### 1.3 Delimitation

The present system block is to be used to protect all types of programmable logic controllers (that is, PLCs and devices that integrate the same or similar functions). It supplements the module IND.2.1 * General ICS Component *. In the application this is therefore also to be considered.

The module contains no organizational requirements for securing an ICS component. For this, the requirements of the block IND.1 * Operating and Control Technology * must be implemented. Similarly, the area of ​​functional safety (safety) is not covered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of PLC:

### 2 1 Incomplete documentation

Programmable logic controllers are often incompletely documented, so not all product functions are known. Information about the services used, protocols and communication ports as well as authorization management are often particularly incomplete. However, this makes the risk analysis more difficult because interfaces, functions and security-relevant mechanisms are overlooked. As a result, potential hazards can not be taken into account. In addition, it can not or only partially react to new vulnerabilities, if this is not detected.

3 requirements
---------------
The following are specific requirements for the PLC area. Basically, the ICS Information Security Officer (ICS-ISB) is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the defined security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.