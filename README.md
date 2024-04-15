# Raspberry Pi Flood Detector

This project implements a flood detection system using a Raspberry Pi connected to a water level sensor. When water is detected, the system sends an email alert to the user and changes the color of Philips Hue lights to blue as a visual indicator. This setup is ideal for basements, bathrooms, or any areas at risk of flooding.

## Description

The flood detector continuously monitors the water level through a sensor connected to a Raspberry Pi. If the sensor detects water, the system uses the Philips Hue API to change the home light color to blue, signaling an alert. It also sends an email notification to the user, ensuring immediate awareness of the flood condition.

## Setup

### Hardware Requirements

- Raspberry Pi (any model that supports GPIO pins)
- Water level sensor compatible with Raspberry Pi
- Philips Hue lights and bridge
- Internet connection

### Software Requirements

- Raspbian or any Raspberry Pi-compatible OS
- Python 3
- Philips Hue API (provided in the code)
- GPIO library for Raspberry Pi

### Installation and Configuration

1. **Set Up Raspberry Pi:**
   Ensure your Raspberry Pi is set up with the latest version of Raspbian and connected to the internet.

2. **Connect the Water Level Sensor:**
   Connect the water level sensor to GPIO pin 18 on your Raspberry Pi.

3. **Install Required Libraries:**
   Install the necessary Python libraries for handling GPIO pins and making HTTP requests.

   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install RPi.GPIO requests
   ```

Configure Philips Hue Bridge:
Ensure your Philips Hue bridge is set up and you have the bridge IP, light ID, and a user token (USERNAME). Update these details in your config.py file:

```python
BRIDGE_IP = 'your_bridge_ip'
LIGHT_ID = 'your_light_id'
USERNAME = 'your_api_key'
```

Run the Detector Script:
To start the flood detection system, run the main.py script:

```bash
python3 main.py
```
