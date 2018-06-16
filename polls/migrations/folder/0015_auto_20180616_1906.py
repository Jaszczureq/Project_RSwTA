# Generated by Django 2.1.dev20180314090007 on 2018-06-16 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0014_auto_20180616_0257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kandydat',
            options={'ordering': ['-votes'], 'verbose_name_plural': 'Kandydaci'},
        ),
        migrations.RemoveField(
            model_name='oddany_glos',
            name='uprawniony',
        ),
        migrations.RemoveField(
            model_name='oddany_glos',
            name='user',
        ),
        migrations.AddField(
            model_name='oddany_glos',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]