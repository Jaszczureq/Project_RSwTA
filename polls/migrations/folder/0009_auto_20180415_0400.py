# Generated by Django 2.1.dev20180314090007 on 2018-04-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20180415_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adres_zamieszkania',
            name='votes',
        ),
        migrations.AddField(
            model_name='kandydat',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='wybor',
            name='kryterium',
        ),
        migrations.AddField(
            model_name='wybor',
            name='kryterium',
            field=models.ManyToManyField(to='polls.Kryterium'),
        ),
    ]
