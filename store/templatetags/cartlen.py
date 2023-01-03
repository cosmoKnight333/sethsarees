from django import template

register = template.Library()
@register.filter(name='cartlen')
def cartlen(customer_id):
    return 78
     