from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(field, classname):
    existing_classes = field.field.widget.attrs.get('class', None)
    if existing_classes:
        if existing_classes.find(given_class) == -1:
            classes = existing_classes + ' ' + classname
        else:
            classes = existing_classes
    else:
        classes = classname
    return field.as_widget(attrs={'class': classes})
