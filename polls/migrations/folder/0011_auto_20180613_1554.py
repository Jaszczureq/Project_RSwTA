# Generated by Django 2.1.dev20180314090007 on 2018-06-13 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_wybor_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wybor',
            name='dataRozpoczecia',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='wybor',
            name='dataZakonczenia',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]