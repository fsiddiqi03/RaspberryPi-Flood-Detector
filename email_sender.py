import boto3
from config import region_name, RECIPIANT, SENDER
from botocore.exceptions import ClientError
from datetime import datetime



class ses():
    def __init__(self):
        self.region = region_name
        self.sender = SENDER
        self.recipiant = RECIPIANT


    def send(self, n):
        ses_client = boto3.client('ses', region_name= self.region)  

        # 0: flood detected, 1: flood no longer detected 
        message = [f'flood detected at {datetime.now()}', f'flood no longer detected at {datetime.now()}']

        try:
            # Provide the contents of the email
            response = ses_client.send_email(
                Source= self.sender,
                Destination={
                    'ToAddresses': [
                        self.recipiant,
                    ],
                },
                Message={
                    'Subject': {
                        'Data': 'Flood Detector',
                    },
                    'Body': {
                        'Text': {
                            'Data': message[n], 
                        },
                    },
                }
            )
        except ClientError as e:
            print(f'Error: {e.response["Error"]["Message"]}')
        else:
            print(f'Email sent! Message ID: {response["MessageId"]}')
    

        
