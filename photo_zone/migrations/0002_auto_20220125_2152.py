# Generated by Django 3.2.5 on 2022-01-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_zone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
