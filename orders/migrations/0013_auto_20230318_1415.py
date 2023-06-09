# Generated by Django 3.2.4 on 2023-03-18 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_user'),
        ('orders', '0012_alter_order_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
    ]
