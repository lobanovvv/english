# Generated by Django 4.0.5 on 2022-06-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_rename_countrynationalitieslanguage_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='oxford_chapter',
            field=models.CharField(max_length=10),
        ),
    ]
