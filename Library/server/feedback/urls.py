from django.urls import include, re_path, path

from .views import *

app_name = 'feedback'
urlpatterns = [
    re_path(r'^$', feedback, name='feedback'),
]