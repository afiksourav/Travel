# Generated by Django 3.2.7 on 2021-10-01 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_package_gallery_package_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_gallery',
            old_name='package_item',
            new_name='package_items',
        ),
    ]
