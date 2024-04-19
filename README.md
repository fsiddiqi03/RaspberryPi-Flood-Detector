# Raspberry Pi Flood Detector

This project implements a flood detection system using a Raspberry Pi connected to a water level sensor. When water is detected, the system sends an email alert to the user and changes the color of Philips Hue lights to blue as a visual indicator. This setup is ideal for basements, bathrooms, or any areas at risk of flooding.

## Description

The flood detector continuously monitors the water level through a sensor connected to a Raspberry Pi. If the sensor detects water, the system uses the Philips Hue API to change the home light color to blue, signaling an alert. It also sends an email notification to the user, ensuring immediate awareness of the flood condition.

## Setup

### Hardware Requirements

- Raspberry Pi (any model that supports GPIO pins)
- Water level sensor compatible with Raspberry Pi: [The one I used](https://www.amazon.com/CQRobot-Consumption-Resistance-Temperature-Properties/dp/B07ZMGW3QJ/ref=sr_1_4?crid=18SF5O5IFZQP4&dib=eyJ2IjoiMSJ9.yIT416c4kLXdQLTHp03Eu1svIEX4cEnA_v11ELozZPsXKbVxdMZMH2G_C8pdT8ndZd0pdPQBbeCVQ9r4M_KVnFZwg_kCM1-q5t4VxzG5bz8MB1WOgd_aatoU9iNT_euXc_lznAhbYb7laI8QH1fqAmK7ZlYRqGWSibg5xGaJALvX5J9qOL1cVoTKR-7JRRfnMiMuyunQFWgTFYo3I0PzeXiItiel6X07E050fBt2yqk.Cl8-H2Pf9xlEBAHeHTiU_J4ZUmI5_rEESKh14xCQR_s&dib_tag=se&keywords=raspberry+pi+water+sensor&qid=1713562844&sprefix=raspberry+pi+water+sensor%2Caps%2C107&sr=8-4)
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
