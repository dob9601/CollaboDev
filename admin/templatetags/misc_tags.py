"""Miscellaneous custom template tags."""
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('bases/debug_warning_base.html')
def debug_warning():
    """Display a warning if CollaboDev is running in debug mode."""
    return {'is_debug': settings.DEBUG}
