import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio import twiml
from twilio.rest import Client
# Create your views here.

def sms_send(msg, recipients):
    twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    client = Client(twilio_account_sid, twilio_auth_token)
    for recipient in recipients:
        message = client.messages.create(
            body=msg,
            from_=twilio_number,
            to=recipient
        )


@csrf_exempt
def sms_reply(request):
    response = twiml.Response()
    msg = response.message("Hello world!")
    return HttpResponse(str(response))
