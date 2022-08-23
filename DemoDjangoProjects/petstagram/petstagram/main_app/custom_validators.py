from django.core.exceptions import ValidationError


def only_letters_validator(value_to_validate):
    for char in value_to_validate:
        if char.isdigit():
            raise ValidationError(f'{value_to_validate} should contain only letters')


def validate_image(file_to_validate):
    filesize = file_to_validate.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
