from django import template

register = template.Library()

@register.filter
def hello(value):
    return 'Hello world!'