# Generated by Django 3.2.4 on 2021-11-28 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
                ('cat_slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('category_image', models.ImageField(blank=True, upload_to='photos/category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
