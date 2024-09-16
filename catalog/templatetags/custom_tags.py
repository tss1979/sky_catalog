from django import template

register = template.Library()

@register.filter()
def change_media_path(data):
    if data:
        return f'/media/{data}'
    return '#'