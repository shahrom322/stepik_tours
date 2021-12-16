from django.contrib import admin
from django.urls import path

from tours.views import main_view, departure_view, tour_view, custom_handler404, custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500


urlpatterns = [
    path('', main_view, name='home'),
    path('admin/', admin.site.urls),
    path('departure/<str:departure>', departure_view, name='departure'),
    path('tour/<int:primary_key>', tour_view, name='tour'),
]
