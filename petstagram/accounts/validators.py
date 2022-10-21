from django.core.exceptions import ValidationError


def validate_isalpha(value):
    if not value.isalpha():
        raise ValidationError('Name can only contain letters.')
