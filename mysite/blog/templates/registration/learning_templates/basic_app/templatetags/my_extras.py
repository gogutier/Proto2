from django import template

register = template.Library()

#escribo una funció que es mi custom template filter
@register.filter(name='cut')
def cut(value,  arg):
    """
    corta los datos values de arg del string

    """
    return value.replace(arg, '')

#register.filter('cut', cut)
