# Generated by Django 2.2.7 on 2019-12-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleasantPup_app', '0008_auto_20191204_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogprofile',
            name='image_link',
        ),
        migrations.AddField(
            model_name='dog',
            name='image_link',
            field=models.TextField(default='No image provided'),
        ),
        migrations.AlterField(
            model_name='breed',
            name='image_link',
            field=models.TextField(default='No image provided'),
        ),
    ]
