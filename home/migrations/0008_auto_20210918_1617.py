# Generated by Django 3.2.7 on 2021-09-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210917_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
