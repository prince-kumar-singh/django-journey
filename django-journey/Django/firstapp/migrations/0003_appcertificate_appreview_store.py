# Generated by Django 5.2 on 2025-04-13 09:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_firstappvarity_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='firstapp.firstappvarity')),
            ],
        ),
        migrations.CreateModel(
            name='AppReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='firstapp.firstappvarity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('app_varity', models.ManyToManyField(related_name='stores', to='firstapp.firstappvarity')),
            ],
        ),
    ]
