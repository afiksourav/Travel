# Generated by Django 3.2.7 on 2021-10-01 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20211002_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_gallery',
            name='package_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.packagedetail_place'),
        ),
    ]
