# Generated by Django 3.0 on 2019-12-04 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=200)),
                ('health_info', models.CharField(max_length=40000)),
                ('image_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_link', models.TextField()),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeds', to='pleasantPup_app.Breed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
