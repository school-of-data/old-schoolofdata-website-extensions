from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter("markdown")
def markdown_filter(s):
  return mark_safe(markdown.markdown(s))
