# Generated by Django 3.2.7 on 2021-09-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_booking_user_place_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
