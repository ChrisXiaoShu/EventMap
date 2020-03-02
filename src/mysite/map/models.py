from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class DisplayManage(models.Manager):

    def get_all_event(self, start_time= datetime.now(), time_delta=timedelta(days=30)):
        end_time = start_time + time_delta
        return self.filter(event_start_time__gte=start_time, event_start_time__lte=end_time)

class EventGeomapData(models.Model):

    u""" Event Geomap Data """

    event_title = models.CharField(max_length=256, help_text=u"事件名稱",null=True)
    event_href = models.URLField(max_length=250,null=True)
    event_start_time = models.DateTimeField(help_text=u"事件開始時間 (CST)",null=True)
    event_end_time = models.DateTimeField(help_text=u"事件結束時間 (CST)",null=True)
    event_addr = models.CharField(max_length=256, help_text=u"事件地址",null=True)
    event_lat = models.DecimalField(max_digits=12, decimal_places=9, verbose_name=u"事件緯度",null=True)
    event_lon = models.DecimalField(max_digits=12, decimal_places=9, verbose_name=u"事件經度",null=True)
    created_date = models.DateTimeField(auto_now_add=True, help_text=u"建立時間",null=True)
    objects = models.Manager()
    display = DisplayManage()

    def __str__(self):
        event_title = self.event_title if self.event_title else "event_title"
        event_href = self.event_href if self.event_href else "event_href"
        return '{} {}'.format(event_title, event_href)

class ClientJobs(models.Model):

    u""" Client Job Data """
    job_name = models.CharField(max_length=256, help_text=u"任務名稱", null=True)
    cron_regex = models.CharField(max_length=256, help_text=u"執行時間規則", null=True)
    next_time = models.DateTimeField(help_text=u"下次執行時間", null=True)

    def __str__(self):
        job_name = self.job_name if self.job_name else "job_name"
        next_time = self.next_time.strftime('%Y-%m-%d %H:%M') if self.next_time else "next_time"
        cron_regex = self.cron_regex
        return '{} {} {}'.format(job_name, next_time, cron_regex)