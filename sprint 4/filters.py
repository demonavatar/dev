from django import template

register = template.Library()


@register.filter
def uglify(text):
    filter_text = ''
    for counter in range(0, len(text)):
        if (counter % 2) != 0:
            filter_text += text[counter].upper()
        else:
            filter_text += text[counter].lower()
    return filter_text
