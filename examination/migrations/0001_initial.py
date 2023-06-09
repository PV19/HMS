# Generated by Django 4.0.3 on 2022-06-10 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OPD_Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_examination', models.CharField(max_length=500)),
                ('dre', models.CharField(max_length=500)),
                ('systematic_examination', models.CharField(max_length=500)),
                ('UHID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='++', to='homepage.homepagemodel')),
            ],
        ),
    ]
