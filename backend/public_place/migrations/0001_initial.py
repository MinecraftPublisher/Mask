# Generated by Django 4.1 on 2022-08-11 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('region', models.PositiveSmallIntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('W', 'White'), ('R', 'Red')], max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_place.publicplace')),
            ],
        ),
        migrations.CreateModel(
            name='MeetPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_user', models.PositiveSmallIntegerField(choices=[(1, 'Healthy'), (2, 'Doubtful'), (3, 'Perilous'), (4, 'Patient'), (5, 'Dead')])),
                ('status_Place', models.PositiveSmallIntegerField(choices=[('W', 'White'), ('R', 'Red')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='public_place.publicplace')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general_user.generaluser')),
            ],
        ),
    ]
