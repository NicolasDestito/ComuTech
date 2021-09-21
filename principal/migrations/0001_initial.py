# Generated by Django 3.2.7 on 2021-09-21 19:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ending_date', models.DateTimeField(blank=True)),
                ('state', models.CharField(choices=[('A', 'Aberto'), ('C', 'Congelado'), ('F', 'Finalizado')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='AidType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('phone', models.CharField(max_length=13)),
                ('cep', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('birth_date', models.DateField()),
                ('password', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(blank=True, upload_to='usuarios/')),
                ('whatsapp', models.CharField(max_length=13)),
                ('twitter', models.CharField(blank=True, max_length=15, validators=[django.core.validators.MinLengthValidator(4)])),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=30)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AidPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='socorros/')),
                ('description', models.TextField(blank=True)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.aid')),
            ],
        ),
        migrations.AddField(
            model_name='aid',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador', to='principal.user'),
        ),
        migrations.AddField(
            model_name='aid',
            name='contributors',
            field=models.ManyToManyField(related_name='contribuidores', to='principal.User'),
        ),
        migrations.AddField(
            model_name='aid',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.aidtype'),
        ),
    ]
