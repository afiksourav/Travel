# Generated by Django 3.2.7 on 2021-10-04 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20211004_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.userinfo'),
            preserve_default=False,
        ),
    ]
