from django.shortcuts import render
from .models import Message
# Create your views here.


def chat(request):
    messages_object = Message.objects.all()
    messages_list = []
    for message in messages_object:
        message_struct = {'Sender': message.sender,
                          'Body': message.body,
                          'Sent_at': message.sent_at}
        messages_list.append(message_struct)
    context = {'Chat': messages_list}
    return render(request, 'chat/message-box.html', context=context)
