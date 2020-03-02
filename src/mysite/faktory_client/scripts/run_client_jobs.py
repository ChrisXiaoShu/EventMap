# fclient.py
from datetime import datetime
import time
import requests
import json
from os.path import join, dirname
import logging
import logging.handlers
import os

from bs4 import BeautifulSoup
import faktory
from croniter import croniter
from map.models import ClientJobs
from map.models import EventGeomapData


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
    formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] <%(module)s %(funcName)s %(lineno)d> %(message)s')
    timedrotatingfilehandler.setFormatter(formatter)
    streamhandler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(timedrotatingfilehandler)
    if print_log:
        logger.addHandler(streamhandler)
    return logger


def get_jobs(datetime_now):
    """get job the next_time < datetime_now"""
    return ClientJobs.objects.filter(next_time__lte=datetime_now)

def set_next_time(job):
    cron_iter = croniter(job.cron_regex, datetime.now())
    job.next_time = cron_iter.get_next(datetime)
    job.save()

# Create client job from here.
def test_job():
    with faktory.connection() as client:
        client.queue('test_job', args=('test_success',),)

#every month
def crawl_taipei_job():
    print('do crawl_Taipei_job')
    with faktory.connection(faktory="tcp://faktory:7419") as client:
        now = datetime.now()
        url = 'https://www.travel.taipei/zh-tw/event-calendar/{}'.format(now.year)
        client.queue('crawl_taipei', args=(url,), queue='crawl_taipei')

#every two week
def run_google_API():
    print('run_google_API')
    with faktory.connection(faktory="tcp://faktory:7419") as client:
        Qset = EventGeomapData.objects.filter(event_lat=None, event_lon=None)
        for event in Qset:
            if event.event_addr is not None:
                client.queue('googleAPI', args=(event.id, event.event_addr), queue='get_geocode')
  

def dump_eventmap_json():
    print('dump_json')
    events = EventGeomapData.objects.all().exclude(event_lat=None, event_lon=None)

    result = list()
    for event in events:
        event_dic = {}
        event_dic['location'] = event.event_addr
        event_dic['start_time'] = event.event_start_time.strftime('%Y-%m-%d')
        event_dic['end_time'] =event.event_end_time.strftime('%Y-%m-%d')
        event_dic['title'] = event.event_title
        event_dic['href'] = event.event_href
        event_dic['latitude'] = float(event.event_lat)
        event_dic['longitude'] = float(event.event_lon)
        result.append(event_dic) 

    json_path = join(dirname(__file__), 'points.json')
    with open(json_path, 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False)
    
    
#key are the job name in ClientJobs table
JOBMAPPING = {'crawl_taipei_job' : crawl_taipei_job,'run_google_API' : run_google_API, 'dump_eventmap_json' : dump_eventmap_json}


def run():
    clientlog = set_logger('./run_client_job.log', log_level='DEBUG')
    current_jobs = get_jobs(datetime.now())
    for job in current_jobs:
        clientlog.info('{}'.format(job))
        JOBMAPPING[job.job_name]()
        set_next_time(job)
        
