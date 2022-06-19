# Generated by Django 4.0.5 on 2022-06-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryNationalitiesLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('nationalities', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('oxford_exist', models.BooleanField(default=False)),
            ],
        ),
    ]
