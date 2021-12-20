import random

from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render

from .tours import title, subtitle, description, departures, tours


def main_view(request):
    random_tours = dict(random.sample(tours.items(), 6))
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
    tours_by_departure = dict(filter(lambda x: x[1]['departure'] == departure, tours.items()))

    max_nights = max(tours_by_departure.values(), key=lambda x: x['nights'])['nights']
    min_nights = min(tours_by_departure.values(), key=lambda x: x['nights'])['nights']

    min_price = min(tours_by_departure.values(), key=lambda x: x['price'])['price']
    max_price = max(tours_by_departure.values(), key=lambda x: x['price'])['price']

    tours_count = len(tours_by_departure)

    return render(
        request,
        'departure.html',
        {
            'departure': departure,
            'tours_by_departure': tours_by_departure,
            'departures': departures,
            'count': tours_count,
            'min_price': min_price,
            'max_price': max_price,
            'min_nights': min_nights,
            'max_nights': max_nights,
        }
    )


def tour_view(request, primary_key):
    tour = tours.get(primary_key)
    tour_departure = departures.get(tour['departure'])

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
