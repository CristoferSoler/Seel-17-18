Table of content

[toc]
 
1 description
--------------

### 1.1 Introduction

Sensors are microprocessors and software electronic transmitters that convert a physical quantity into an electrical output value. This is provided as a standard standardized signal (often 4 to 20 mA, 0 to 10 V) as data on a serial interface or as digital information transmitted over a fieldbus or Ethernet protocols. In addition to the measured values, transducers frequently provide interfaces via which a diagnosis and parameterization takes place. So a sensor in addition to an electronic output value can also have other interfaces, z. WLAN, Bluetooth or wireless HART interfaces for parameterization and diagnostics.

There are many different sensors on the market. To measure physical quantities. Depending on the task, the functionality and performance of a sensor vary greatly. The spectrum ranges from sensors that only deliver readings and do not need to be configured, to those that allow calibration, configuration or preprocessing of data through to full signal processing (smart sensors).

### 1.2 Objective

The goal of the device is to protect all types of intelligent sensors, regardless of manufacturer, type, purpose and location. It can be applied to a single sensor or a contiguous assembly used as a sensor.

### 1.3 Delimitation

The present system block is to be used to secure intelligent sensors. It supplements and presupposes the higher-level module IND.2.1 * General ICS Component *.

Simple sensors without configuration interfaces or more complex processing logic are not detected by the module, since the possible protective measures are limited to securing access to the sensor and monitoring whether it is active.

Also, the device does not address the protection of complex wireless sensor networks. It merely describes how individual sensors can be protected. Furthermore, no safety requirements for operating and control technology are described. For this, the block IND.1 * Operating and Control Technology * must be implemented.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of sensors:

### 2 1 Insufficient security requirements for procurement

Due to a lack of awareness of the risks and cost reasons, information security is often not taken into account in procurement. As a result, sensors can sometimes contain serious weaknesses that can only be remedied with great difficulty later on.

Sensors for ICS components in industrial environments are often exposed to special conditions that may affect safe operation. Examples include extreme heat, cold, moisture, dust, vibration or corrosive or corrosive atmospheres. Frequently, several factors occur simultaneously. Such adverse environmental effects can cause the sensors of ICS components to wear faster and fail earlier or measure erroneous values.

3 requirements
---------------

The following are specific requirements for the sensors area. Basically, the ICS Information Security Officer (ICS-ISB) is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the defined security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.
