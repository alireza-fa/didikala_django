from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


def check_phone_number(value):
    if len(value) > 11 or len(value) < 11 or not value.startswith('09'):
        raise ValidationError(_('This phone number you entered is not a valid phone number.'))
