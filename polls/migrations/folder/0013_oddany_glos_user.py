# Generated by Django 2.1.dev20180314090007 on 2018-06-15 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0012_auto_20180615_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='oddany_glos',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
