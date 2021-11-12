from django.http import HttpResponseBadRequest, HttpResponseServerError

from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html')


def departure_view(request):
    return render(request, 'departure.html')


def tour_view(request):
    return render(request, 'tour.html')


def custom_handler404(request, exception):
    return HttpResponseBadRequest('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
