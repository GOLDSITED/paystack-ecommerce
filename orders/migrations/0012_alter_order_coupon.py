# Generated by Django 3.2.4 on 2022-05-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_promocode_usage_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]