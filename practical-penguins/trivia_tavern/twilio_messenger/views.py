import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio import twiml
from twilio.rest import Client
# Create your views here.

answers = {
    'answer': '4',
    'correct': 'Correct!',
    'incorrect': 'How could you know? We didn\'t tell you what kind!'
}

def sms_send(msg, recipients):
    """sms_send will send a message 'msg' to a list of recipients 'recipients'
    This is not really a view method, but a help method for other classes
    and views (for example the user views)
    """
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
    recipients = request.POST.get('From', None)
    body = request.POST.get('Body', None)

    #response = twiml.Response()

    if body == answers['answer']:
        msg = answers['correct']
    else:
        msg = answers['incorrect']
    sms_send(msg, [recipients])
    # This will need to be changed to track response for errors, but not sure
    # exactly how to implement since twiml.response doesn't seem to work
    return HttpResponse(200)
