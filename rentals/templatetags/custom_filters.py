# rentals/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies value by arg"""
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0  # Return 0 if multiplication fails
