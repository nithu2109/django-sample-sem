# Generated by Django 3.2.9 on 2022-02-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busid', models.IntegerField()),
                ('bustype', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('startingat', models.TimeField()),
                ('willreachat', models.TimeField()),
                ('stops', models.CharField(max_length=30)),
                ('drivername', models.CharField(max_length=30)),
                ('conductorname', models.CharField(max_length=30)),
            ],
        ),
    ]
