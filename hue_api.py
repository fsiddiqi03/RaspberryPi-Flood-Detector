import json
import requests
from config import BRIDGE_IP, LIGHT_ID, USERNAME



class hueAPI():
    def __init__(self):
        self.bridgeIP = BRIDGE_IP
        self.lightID = LIGHT_ID
        self.username = USERNAME
        self.headers = {"hue-application-key": self.username}
        self.url = f"https://{self.bridgeIP}/clip/v2/resource//light/{self.lightID}"


    def lightStatus(self):
        try:
            response = requests.get(self.url, headers=self.headers, verify=False)
            if response.status_code == 200:
                data = response.json()
                lightStatus = data['data'][0]['on']['on']
                return lightStatus
            else:
                print('failed to get status')
        except Exception as e:
            print(e)


    def turnON(self):
        payload = json.dumps({
            "on": {
                "on": True
            }
        })

        if not self.lightStatus():
            try:
                response = requests.put(self.url, headers=self.headers, data=payload, verify=False)
                if response.status_code == 200:
                    return True
                else: 
                    return False
            except Exception as e:
                print(e)
                return False 
        else:
            print('lights already on')
            return True
        
        
    def brightness(self, percent):
        payload = json.dumps({
            "dimming": {
                "brightness": percent
            }
        })

        try:
            response = requests.put(self.url, headers=self.headers, data=payload, verify=False)
            if response.status_code == 200:
                print('brightness changed')
                return True
            else:
                print('failed')
                return False
        except Exception as e:
            print(e)


    def changeColor(self):
        # if light not on turn it on 
        if not self.lightStatus():
            self.turnON()
        
        self.brightness(100)
        
        payload = json.dumps({
            "color": {
                "xy": {
                    "x": 0.15,
                    "y": .20
                }
            }

        })
        try:
            response = requests.put(self.url, headers=self.headers, data=payload, verify=False)
            if response.status_code == 200:
                print('color changed')
                return True
            else:
                print('failed')
                return False
        except Exception as e:
            print(e)

