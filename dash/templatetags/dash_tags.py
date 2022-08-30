# dash.templetags.dash_tags.py

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def current_link_active(context, name):
    if context['request'].resolver_match.url_name == name:
        return 'active'
    return ''
