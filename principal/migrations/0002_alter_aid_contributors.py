# Generated by Django 3.2.7 on 2021-09-25 22:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='contributors',
            field=models.ManyToManyField(blank=True, related_name='contribuidores', to=settings.AUTH_USER_MODEL),
        ),
    ]