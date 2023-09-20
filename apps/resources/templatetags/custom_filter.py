from django import template

# Singleton
register = template.Library()


@register.filter
def dash_separator(value):
    return value.replace(", ", "-")


@register.filter
def separator(value, sep):
    return value.replace(", ", sep)
