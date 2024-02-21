# Generated by Django 4.2.10 on 2024-02-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('external_id', models.CharField(max_length=255, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category', models.CharField(max_length=255)),
                ('ratings', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]