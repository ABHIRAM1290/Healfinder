# Generated by Django 5.0.4 on 2024-06-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='docter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dpt', models.CharField(max_length=20)),
                ('exp', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('img', models.FileField(upload_to='')),
                ('hospital', models.CharField(max_length=100)),
                ('con_no', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('st_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_avail', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cno', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('rating', models.IntegerField()),
                ('long', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('reson', models.CharField(max_length=100)),
                ('visit_hos', models.CharField(max_length=100)),
                ('visit_doc', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
    ]
