import boto3
from config import region_name, RECIPIANT, SENDER
from botocore.exceptions import ClientError
from datetime import datetime



class ses():
    def __init__(self):
        self.region = region_name
        self.sender = SENDER
        self.recipiant = RECIPIANT


    def send(self):
        ses_client = boto3.client('ses', region_name= self.region)  

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
                            'Data': f'flood detected at {datetime.now()}', 
                        },
                    },
                }
            )
        except ClientError as e:
            print(f'Error: {e.response["Error"]["Message"]}')
        else:
            print(f'Email sent! Message ID: {response["MessageId"]}')
    

        
