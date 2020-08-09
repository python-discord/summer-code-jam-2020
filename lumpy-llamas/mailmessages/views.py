from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse

from core.helpers import jsonbody
from .models import PrivateMessage

MESSAGE_SCHEMA = {
    'type': 'object',
    'required': ['to_user', 'subject', 'message'],
    'properties': {
        'to_user': {
            'type': 'string',
            'minLength': 1,
        },
        'subject': {
            'type': 'string',
            'minLength': 1,  # just for the jam, make things quicker
        },
        'message': {
            'type': 'string',
            'minLength': 1,  # just for the jam, make things quicker
        },
    },
}


def list_messages(request):
    current_user = request.user.username
    queryset = PrivateMessage.objects.filter(Q(to_user=request.user.username) | Q(from_user=request.user.username)). \
        values('message', 'subject', 'created_date', 'from_user', 'to_user', 'id').order_by('-created_date')
    data = list(queryset)
    json_data = {'query': data, 'current_user': current_user}

    return JsonResponse(json_data, status=201, safe=False)


def get_users(request):
    queryset = User.objects.values('id', 'username').filter(~Q(username=request.user.username))
    data = list(queryset)

    return JsonResponse(data, status=201, safe=False)


@jsonbody(MESSAGE_SCHEMA)
def post_message(request, data):
    current_user = request.user
    to_user = User.objects.get(username=data['to_user'])
    if to_user is not None:
        message = PrivateMessage(
            message=data['message'],
            subject=data['subject'],
            from_user=current_user,
            to_user=to_user,
        )
        message.save()

        return JsonResponse({
            'message_id': message.id,
            'message': message.message,
            'subject': message.subject,
        }, status=201)
