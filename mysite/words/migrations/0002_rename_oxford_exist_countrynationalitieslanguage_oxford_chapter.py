# Generated by Django 4.0.5 on 2022-06-20 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countrynationalitieslanguage',
            old_name='oxford_exist',
            new_name='oxford_chapter',
        ),
    ]