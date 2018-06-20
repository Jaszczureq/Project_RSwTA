from django import template

register = template.Library()


@register.filter(name='div')
def div(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg:
            return value / arg
    except:
        pass
    return ''


@register.filter(name='div')
def mul(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg:
            return value * arg
    except:
        pass
    return ''


register.filter('div', div)
register.filter('mul', mul)
