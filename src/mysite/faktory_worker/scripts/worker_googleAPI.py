
import time
import os
from os.path import join, dirname

import googlemaps
from dotenv import load_dotenv
import faktory
#in order to use django envirunment
import django
django.setup()
from map.models import EventGeomapData

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)

GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_PLACES_API_KEY)


def get_geocode(_id, addr):
    geocode_result = gmaps.geocode(addr)
    lat = None
    lng = None
    if geocode_result is not None:
        lat = geocode_result[-1]['geometry']['location']['lat']
        lng = geocode_result[-1]['geometry']['location']['lng']

    EventGeomapData.objects.filter(id=_id).update(event_lat=lat, event_lon=lng)
    time.sleep(1)


def run():
    w = faktory.Worker(faktory="tcp://faktory:7419", queues=['get_geocode',], concurrency=1)
    w.register('googleAPI', get_geocode)
    w.run()


if __name__ == "__main__":
    run()