# Generated by Django 2.2.7 on 2019-12-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleasantPup_app', '0009_auto_20191204_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='age',
            field=models.TextField(default=0),
        ),
        migrations.DeleteModel(
            name='DogProfile',
        ),
    ]
