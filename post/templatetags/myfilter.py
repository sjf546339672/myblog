# coding: utf-8
from django import template
register = template.Library()


@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)
