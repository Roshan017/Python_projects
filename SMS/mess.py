from twilio.rest import Client

account_sid = 'AC55db7ae8ee79dc91c533df0c8c70bdc7'
auth_token = '37b772c23b08277233d243dbf7d21022'
client = Client(account_sid, auth_token)



msg_body = input("Enter the message to be send: ")
message = client.messages.create(
from_='+17165881914',
body= msg_body,
to='+919188470265'
    )
print(message.sid)

