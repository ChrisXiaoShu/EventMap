# rainmonitor urls 
from django.conf.urls import url
from map.views import map_index


urlpatterns = [
    url(r'^', map_index),
]
