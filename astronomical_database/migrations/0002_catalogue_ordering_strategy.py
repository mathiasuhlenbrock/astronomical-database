# Generated by Django 2.2.12 on 2020-05-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronomical_database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='ordering_strategy',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
