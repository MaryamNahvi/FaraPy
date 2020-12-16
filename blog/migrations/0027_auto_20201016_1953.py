# Generated by Django 2.2.7 on 2020-10-16 16:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20201016_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(0, 'Primary Menu'), (1, 'Secondry Menu')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (0, 'Female')], default=1, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='subtickets',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='created_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 16, 19, 53, 38, 361377), null=True, verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 16, 19, 53, 38, 361377), null=True, verbose_name='Finish date'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='status',
            field=models.IntegerField(choices=[(1, 'In progress'), (3, 'Done!'), (0, 'To Do')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='time',
            name='status',
            field=models.IntegerField(choices=[(0, 'On Duty'), (1, 'Out of Duty')], default=0, verbose_name='Status'),
        ),
    ]
