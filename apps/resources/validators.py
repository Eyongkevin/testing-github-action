from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_rating_range(value):
    if value < 0 or value > 5:
        raise ValidationError(_("%(value)s is not valid", params={"value": value}))
