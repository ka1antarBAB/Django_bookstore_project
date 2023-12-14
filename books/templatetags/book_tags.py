from django import template

register = template.Library()
# lowercase


@register.filter
def to_title(value, arg):
    return f"{arg.upper()}: {value.title()}"
