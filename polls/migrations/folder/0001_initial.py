# Generated by Django 2.1.dev20180314090007 on 2018-04-07 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres_zamieszkania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAdresZamieszkania', models.IntegerField()),
                ('ulica', models.CharField(max_length=255)),
                ('numerBudynku', models.CharField(max_length=5)),
                ('numerLokalu', models.CharField(max_length=5)),
                ('kodPocztowy', models.CharField(max_length=6)),
                ('miejscowosc', models.CharField(max_length=255)),
                ('idKraj', models.IntegerField()),
            ],
        ),
    ]