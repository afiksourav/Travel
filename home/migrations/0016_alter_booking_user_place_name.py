# Generated by Django 3.2.7 on 2021-09-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_booking_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_user',
            name='place_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district_specific_place'),
        ),
    ]
