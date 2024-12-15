from django import template

register = template.Library()

@register.filter
def censor(value):
    bad_words = ['редиска', 'фуфло']
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value
