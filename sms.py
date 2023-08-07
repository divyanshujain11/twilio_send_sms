# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'Account_sid'
auth_token = 'auth_token'
  
client = Client(account_sid, auth_token)
message = client.messages.create(
                              from_='++17693009632',
                              body ='body',
                              to ='+918107996387'
                          )
  
print(message.sid)
