from django.urls import path, include
from products.views import (favorites_list, add_to_favorites, remove_from_favorites, favorites_api
)


app_name = 'favorites'

urlpatterns = [
        path('', favorites_list, name='list'),
        path('add/', add_to_favorites, name='add'),
        path('remove/', remove_from_favorites, name='remove'),
        path('api/',  favorites_api, name='api'),
]