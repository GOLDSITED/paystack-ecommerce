# Generated by Django 3.2.4 on 2022-05-04 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_is_superadmin_account_is_superuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_superuser',
            new_name='is_superadmin',
        ),
    ]
