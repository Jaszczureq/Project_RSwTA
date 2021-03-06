# Generated by Django 2.1.dev20180314090007 on 2018-04-15 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180414_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='osoba',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Osoba'),
        ),
        migrations.AlterField(
            model_name='oddany_glos',
            name='uprawniony',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Uprawniony'),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='adresZamieszkania',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Adres_zamieszkania'),
        ),
        migrations.AlterField(
            model_name='uprawniony',
            name='osoba',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Osoba'),
        ),
        migrations.AlterField(
            model_name='wybor',
            name='kryterium',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Kryterium'),
        ),
    ]
