from django import template

register=template.Library()

@register.filter
def get_val(dict, key):
    return dict.get(key)