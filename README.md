# Smart Air Safety Monitor

A low-cost home safety monitoring system built with a Raspberry Pi that detects unsafe air conditions such as smoke, gas, and poor air quality. The system continuously monitors sensor readings and provides real-time spoken alerts through a speaker system.

---

## Creator statement

The Smart Air Safety Monitor was created to explore how inexpensive hardware can be used to build a practical air monitoring system. Many commercial home safety devices work like “black boxes,” where people only see the final result and do not understand how the sensors or alerts actually work. One goal of this project was to better understand and show the process behind these systems by building one from simple and accessible parts.

What interested me most was not just whether the device could work, but how useful and reliable a low-cost system could realistically be. The project showed that it is possible to build a meaningful air monitoring device without expensive professional equipment. Using a Raspberry Pi, Grove sensors, and open-source Python libraries, the system could continuously monitor air conditions and automatically respond when readings became unsafe

---
## Overview

The Smart Air Safety Monitor is designed as an affordable environmental monitoring device for home use. Using a Raspberry Pi 3 with Grove sensors, the system detects changes in air quality and gas concentration and responds with automatic voice warnings and alarms.

The project combines:

* Hardware setup
* Python programming
* Sensor communication
* Text-to-speech audio alerts

---

## Features

* Detects air pollution and gas/smoke-related pollution
* Real-time voice announcements
* Automatic warning mode when unsafe gas levels are detecteted
* Continuous live monitoring

---

## Hardware Components

### Computing

* Raspberry Pi 3

### Sensors & Interface

* GrovePi+
* Grove Air Quality Sensor v1.3
* Grove Gas Sensor MQ3

### Audio System

* Passive speaker
* 3.5mm audio cable
* LM386 amplifier circuit

### Amplifier Components

* LM386 amplifier chip
* Breadboard
* Jumper wires
* 100μF capacitors ×2
* 1000μF capacitor
* 10μF capacitor
* 100nF capacitor
* 10Ω resistor
* 10kΩ potentiometer

---

## Software & Technologies

* Python
* Raspberry Pi OS
* GrovePi Python library
* I2C communication
* `espeak` text-to-speech engine
* `aplay` audio routing
* Git & GitHub

---

## System Architecture

The Python monitoring program continuously:

1. Reads analog sensor values
2. Classifies air quality conditions
3. Detects unsafe gas levels
4. Sends spoken announcements through the speaker
5. Activates warning mode when thresholds are exceeded


---

## Hardware Setup

### Sensor Connections

* Air Quality Sensor → A0
* MQ3 Gas Sensor → A1

### Amplifier Setup

The Raspberry Pi’s headphone jack output was too weak to directly power the passive speaker. To solve this, an LM386 amplifier circuit was built on a breadboard.


## Installation

### Clone Repository

```bash
git clone <repository-url>
cd smart-air-safety-monitor
```

### Install GrovePi Library

```bash
git clone https://github.com/DexterInd/GrovePi.git
cd GrovePi/Software/Python
sudo pip3 install .
```

### Install Audio Dependencies

```bash
sudo apt-get install espeak alsa-utils
```

---

## Running the Project

Run the monitoring program:

```bash
python3 air_quality.py
```


---

## Testing

The MQ3 Gas Sensor is capable of detecting:

* Alcohol
* Benzine
* CH4
* Hexane
* LPG
* CO-related gases

To test the system, alcohol wipes were used to produce strong fumes near the sensor.

### Results

* Sensor readings increased immediately
* Warning mode activated successfully
* Spoken alarms played through the speaker
* System returned to normal mode after readings decreased

---

## Challenges & Fixes

### Low Audio Volume

The Raspberry Pi headphone jack alone could not adequately drive the passive speaker.

### Solution

An LM386 amplifier circuit was designed and built on a breadboard to amplify the audio signal.


## References

- [GrovePi Plus Documentation](https://wiki.seeedstudio.com/GrovePi_Plus/)
- [Grove Gas Sensor MQ3 Documentation](https://wiki.seeedstudio.com/Grove-Gas_Sensor-MQ3/#play-with-raspberry-pi-with-grove-base-hat-for-raspberry-pi)
- [Grove Air Quality Sensor v1.3 Documentation](https://wiki.seeedstudio.com/Grove-Air_Quality_Sensor_v1.3/)



