from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(field, class_attr):
    return field.as_widget(attrs={"class": class_attr})
