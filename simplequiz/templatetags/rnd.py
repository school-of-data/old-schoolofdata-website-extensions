import random
from django import template

register = template.Library()


@register.filter("shuffle")
def shuffle(a):
    return random.sample(a,len(a))
