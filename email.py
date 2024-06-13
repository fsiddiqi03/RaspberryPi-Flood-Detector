import boto3
from config import region_name, RECIPIANT, SENDER
from botocore.exceptions import ClientError


class SendEmail():
    def __init__(self):
        self.region = region_name
        self.sender = SENDER
        self.recipiant = RECIPIANT


    def email(self):
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
                            'Data': 'flood detected at', # create getTime function 
                        },
                    },
                }
            )
        except ClientError as e:
            print(f'Error: {e.response["Error"]["Message"]}')
        else:
            print(f'Email sent! Message ID: {response["MessageId"]}')
    

        
