import time
import os
import requests

from bs4 import BeautifulSoup
import faktory
import logging
import logging.handlers
#in order to use django envirunment
import django
django.setup()
from map.models import EventGeomapData


time.sleep(1)

def check_directory(directory, mode=0o755):
    if not os.path.exists(directory):
        os.makedirs(directory, mode)


def set_logger(logfile, log_level="DEBUG", print_log=False):
    """ Set logger setting.
    Argument:
        logfile - set logging output file.
        log_level - set logging level.
        print_log - bollean, True: print logging information to sys.stdout.
    Return:
        logger - logging.getLogger() object.
    """
    check_directory(os.path.dirname(logfile))
    timedrotatingfilehandler = logging.handlers.TimedRotatingFileHandler(filename=logfile, when="midnight")
    streamhandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] <%(module)s %(funcName)s %(lineno)d> %(message)s')
    timedrotatingfilehandler.setFormatter(formatter)
    streamhandler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(timedrotatingfilehandler)
    if print_log:
        logger.addHandler(streamhandler)
    return logger
    

def crawl_taipei_detail(title, href, start_time, end_time):
    resp = requests.get(href)
    soup = BeautifulSoup(resp.content.decode(resp.encoding), 'html.parser')

    detail = soup.find('a', class_='btn-location-link')
    if not detail:
        detail = soup.find('dl', class_='event-info-list')
        addr = detail.find_all('dd', class_="info")[-1].string.strip()
        lat = None
        lon = None
    else:
        addr = detail.string.strip()
        lat, lon = detail.get('href').split('/')[-1].split(',')

    EventGeomapData.objects.update_or_create(
            event_title = title, event_href = href, event_addr =addr,
            defaults={
                'event_start_time' : start_time,
                'event_end_time' : end_time,  
                'event_lat' : lat,
                'event_lon': lon
            })
    time.sleep(1)
    

def crawl_taipei(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content.decode(resp.encoding), 'html.parser')

    full_event = soup.find("div", class_="full-year-event-blk", id="full-year-event-blk")
    event = full_event.find_all('li', class_="item")

    event_set = set()
    for i in event:
        title = i.find("a").get('title')
        if title in event_set:
            continue
        else:
            event_set.add(title)

        href = '{}{}'.format('https://www.travel.taipei', i.find("a").get("href"))
        event_time = i.find('p', class_='date').string.strip()
        event_time = event_time.split('～')
        if len(event_time)>=2:
            start_time, end_time = event_time
        else:
            start_time = event_time[-1]
            end_time = start_time

        with faktory.connection(faktory="tcp://faktory:7419") as client:
            client.queue('crawl_taipei_detail', args=(title, href, start_time, end_time), queue='crawl_taipei')


def run():
    #worklog = set_logger('./worker_crawl_taipei.log', log_level='DEBUG', print_log=True)
    w = faktory.Worker(faktory="tcp://faktory:7419", queues=['crawl_taipei',], concurrency=1)
    w.register('crawl_taipei', crawl_taipei)
    w.register('crawl_taipei_detail', crawl_taipei_detail)
    w.run()


if __name__ == "__main__":
    run()