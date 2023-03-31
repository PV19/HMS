# Generated by Django 4.0.3 on 2022-07-18 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='opdrxmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicinename', models.CharField(max_length=50)),
                ('doctorname', models.CharField(max_length=50)),
                ('dosage', models.CharField(max_length=50)),
                ('route', models.CharField(max_length=50)),
                ('entreperiod', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
                ('followupinstruction', models.CharField(max_length=500)),
                ('todaydate', models.DateField()),
                ('todaytime', models.TimeField()),
                ('nextfollowupdate', models.DateField()),
                ('nextfollowuptime', models.TimeField()),
                ('opdrx_UHID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.homepagemodel')),
            ],
        ),
    ]