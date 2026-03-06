#Task 2 is about the twilio API
#https://www.twilio.com/

from twilio.rest import Client

#twilio params
#register at https://www.twilio.com/
account_sid = "YOUR_SID"#your SID
auth_token = "YOUR_AUTH_TOKEN" #your Auth token

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="TWILIO_NUMBER",  # add your twilio number
    to="MY_NUMBER",  # add your own number
)

print(message.body)