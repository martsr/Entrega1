# Generated by Django 4.1 on 2022-09-06 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAdmin', '0003_alter_profile_desc_alter_profile_webpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='desc',
            new_name='description',
        ),
    ]
