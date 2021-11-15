import random

from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render

from .tours import title, subtitle, description, departures, tours


def main_view(request):
    random_tours = dict()
    tours_count = 0
    while tours_count != 6:
        choice = random.randint(1, len(tours))
        if choice in random_tours.keys():
            continue
        random_tours[choice] = tours[choice]
        tours_count += 1

    return render(
        request,
        'index.html',
        {
            'tours': random_tours,
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'departures': departures,
        }
    )


def departure_view(request, departure):
    tours_by_departure = dict()
    min_price = float("inf")
    min_nights = float("inf")
    max_price = 0
    max_nights = 0

    for key, tour in tours.items():
        if tour['departure'] == departure:
            tours_by_departure[key] = tour
            if tour['price'] < min_price:
                min_price = tour['price']
            if tour['price'] > max_price:
                max_price = tour['price']
            if tour['nights'] < min_nights:
                min_nights = tour['nights']
            if tour['nights'] > max_nights:
                max_nights = tour['nights']

    count = len(tours_by_departure)

    if isinstance(min_price, int):
        min_price = '{:,}'.format(min_price).replace(',', ' ')
    if isinstance(max_price, int):
        max_price = '{:,}'.format(max_price).replace(',', ' ')

    return render(
        request,
        'departure.html',
        {
            'departure': departure,
            'tours_by_departure': tours_by_departure,
            'departures': departures,
            'count': count,
            'min_price': min_price,
            'max_price': max_price,
            'min_nights': min_nights,
            'max_nights': max_nights,
        }
    )


def tour_view(request, id):
    tour = tours.get(id)
    tour_departure = departures.get(tour['departure'])
    if isinstance(tour['price'], int):
        tour['price'] = '{:,}'.format(tour['price']).replace(',', ' ')
    if '★' not in tour['stars']:
        tour['stars'] = '★' * int(tour['stars'])
    return render(
        request,
        'tour.html',
        {
            'tour': tour,
            'tour_departure': tour_departure,
            'departures': departures,
        }
    )


def custom_handler404(request, exception):
    return HttpResponseBadRequest('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
