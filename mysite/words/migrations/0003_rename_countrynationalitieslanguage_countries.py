# Generated by Django 4.0.5 on 2022-06-20 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_rename_oxford_exist_countrynationalitieslanguage_oxford_chapter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CountryNationalitiesLanguage',
            new_name='Countries',
        ),
    ]