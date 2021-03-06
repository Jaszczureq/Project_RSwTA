# Generated by Django 2.1.dev20180314090007 on 2018-04-14 02:01

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('polls', '0005_auto_20180410_2211'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Kraj',
        ),
        migrations.AlterModelOptions(
            name='adres_zamieszkania',
            options={'verbose_name_plural': 'Adresy_zamieszkania'},
        ),
        migrations.AlterModelOptions(
            name='kandydat',
            options={'verbose_name_plural': 'Kandydaci'},
        ),
        migrations.AlterModelOptions(
            name='kraj',
            options={'verbose_name_plural': 'Kraje'},
        ),
        migrations.AlterModelOptions(
            name='kryterium',
            options={'verbose_name_plural': 'Kryteria'},
        ),
        migrations.AlterModelOptions(
            name='oddany_glos',
            options={'verbose_name_plural': 'Oddane_głosy'},
        ),
        migrations.AlterModelOptions(
            name='osoba',
            options={'verbose_name_plural': 'Osoby'},
        ),
        migrations.AlterModelOptions(
            name='uprawniony',
            options={'verbose_name_plural': 'Uprawnieni'},
        ),
        migrations.AlterModelOptions(
            name='wybor',
            options={'verbose_name_plural': 'Wybory'},
        ),
        migrations.RenameField(
            model_name='adres_zamieszkania',
            old_name='idCountry',
            new_name='Kraj',
        ),
        migrations.RenameField(
            model_name='kandydat',
            old_name='idOsoba',
            new_name='Osoba',
        ),
        migrations.RenameField(
            model_name='kandydat',
            old_name='idWybor',
            new_name='Wybor',
        ),
        migrations.RenameField(
            model_name='kraj',
            old_name='idCountry',
            new_name='idKraj',
        ),
        migrations.RenameField(
            model_name='kraj',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='oddany_glos',
            old_name='idUprawniony',
            new_name='Uprawniony',
        ),
        migrations.RenameField(
            model_name='oddany_glos',
            old_name='idWybor',
            new_name='Wybor',
        ),
        migrations.RenameField(
            model_name='osoba',
            old_name='idAdresZamieszkania',
            new_name='AdresZamieszkania',
        ),
        migrations.RenameField(
            model_name='uprawniony',
            old_name='idOsoba',
            new_name='Osoba',
        ),
        migrations.RenameField(
            model_name='uprawniony',
            old_name='idWybor',
            new_name='Wybor',
        ),
        migrations.RenameField(
            model_name='wybor',
            old_name='idKryterium',
            new_name='Kryterium',
        ),
    ]
