from django.core.exceptions import ValidationError
from datetime import date


def calculate_age(born: date):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def valid_age_validator(arg):
    min_age = 13
    max_age = 100

    age = calculate_age(arg)
    if age <= min_age:
        raise ValidationError(f'You have to be older than {min_age}.')
    elif age > max_age:
        raise ValidationError('Please provide a valid age.')
