# Generated by Django 4.0.6 on 2022-08-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='allow_rating',
            field=models.BooleanField(default=True),
        ),
    ]
