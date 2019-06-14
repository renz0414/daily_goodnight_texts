from twilio.rest import Client
import random
from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=0, minute=30, second=0, microsecond=0) #Sends text at 12:30am
delta_t=y-x
secs=delta_t.seconds+1


def job():
    text_messages = [
        "gn ily",
        "gn cutie",
        "night beautiful",
        "goodnight ugly",
        "sweet dreams",
        "gnight imy"
    ]

    index = random.randrange(0,len(text_messages));

    account_sid = '' #can be found in Twilio Dashboard
    auth_token = '' #can be found in Twilio Dashboard

    myPhone = ''  #Your Phone Number
    TwilioNumber = ''  #Your Twilio Phone Number

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=myPhone,
        from_=TwilioNumber,
        body=text_messages[index])


t = Timer(secs, job)
t.start()

