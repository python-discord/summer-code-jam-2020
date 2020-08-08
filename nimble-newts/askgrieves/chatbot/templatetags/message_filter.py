from django import template
from chatbot.views import Message

register = template.Library()


@register.filter
def text(message: Message) -> str:
    return message.text


@register.filter
def action(message: Message) -> str:
    return message.action
