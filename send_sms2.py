from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account

account_sid = "XXXXXXXXXXXXXXXXXXX" #YOUR SID
auth_token = "XXXXXXXXXXXXXXXXXXXXX" #YOUR TOKEN

message = raw_input("Please enter your message ")

client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+44YOURMOBNUMBER", from_="+44YOURTWILIONUMBER",
                                     body=message) # Enter the number you are sending to and from your Twilio Number

print message.sid
print "Your message is being sent"
print "Check your phone!"

