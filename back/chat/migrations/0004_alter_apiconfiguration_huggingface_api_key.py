# Generated by Django 5.1 on 2024-08-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_apiconfiguration_num_insights_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiconfiguration',
            name='huggingface_api_key',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
