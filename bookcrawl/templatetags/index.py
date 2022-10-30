from django import template
register = template.Library()

@register.filter
def indexi(indexable, i):
    return indexable[i]