# Generated by Django 3.1.5 on 2023-04-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
    ]
