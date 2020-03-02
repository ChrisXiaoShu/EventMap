# Generated by Django 2.2.4 on 2020-01-11 02:32

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventGeomapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(help_text='事件名稱', max_length=256)),
                ('event_href', models.URLField(max_length=250)),
                ('event_start_time', models.DateTimeField(help_text='事件開始時間 (CST)')),
                ('event_end_time', models.DateTimeField(help_text='事件結束時間 (CST)')),
                ('event_addr', models.CharField(help_text='事件地址', max_length=256)),
                ('event_lat', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='事件緯度')),
                ('event_lon', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='事件經度')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='建立時間')),
            ],
            managers=[
                ('display', django.db.models.manager.Manager()),
            ],
        ),
    ]