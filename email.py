import boto3
from config import region_name, RECIPIANT, SENDER

class SendEmail():
    def __init__(self):
        self.region = region_name
        self.sender = SENDER
        self.recipiant = RECIPIANT

    

        
