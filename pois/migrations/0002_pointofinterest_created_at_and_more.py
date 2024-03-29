# Generated by Django 4.2.10 on 2024-02-21 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pois', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
