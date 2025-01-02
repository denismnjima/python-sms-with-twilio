from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
twilio_phone_number = os.getenv('twilio_phone_number')
tagreget_no = os.getenv('tagreget_no')

client = Client(account_sid,auth_token)

message = client.messages.create(
    body='Hello this is a test sms',
    from_=twilio_phone_number,
    to=tagreget_no

)