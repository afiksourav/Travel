# Generated by Django 3.2.7 on 2021-09-17 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_district_details_gallary_district_details_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='district_specific_place',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('country', models.CharField(blank=True, max_length=250)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('Phone_Number', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]