from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all value sof "arg" from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
# this is the same as @register.filter(name='cut')