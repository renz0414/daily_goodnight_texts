from twilio.rest import Client
import random
from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=23, minute=14, second=0, microsecond=0)
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

    account_sid = 'AC78aba76dfcd310f92d2d7fddcbd9730a'
    auth_token = '62fa32adf229516ec6fcbf3a078ea0b6'

    myPhone = '5712670056'
    TwilioNumber = '17272585988'

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=myPhone,
        from_=TwilioNumber,
        body=text_messages[index])


t = Timer(secs, job)
t.start()

