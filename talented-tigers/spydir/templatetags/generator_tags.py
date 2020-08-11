from django import template

register = template.Library()


@register.filter()
def split_content(value):
    return [paragraph for paragraph in value.split("\n")]


@register.filter()
def mod(value, argument):
    return value % argument
