from django import template

register = template.Library()


def get_number_format(number) -> str:
    return '{:,}'.format(number).replace(',', ' ')


def get_stars_format(number) -> str:
    return '★' * int(number)


register.filter('get_number_format', get_number_format)
register.filter('get_stars_format', get_stars_format)