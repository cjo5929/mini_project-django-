# Generated by Django 4.0.1 on 2022-01-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_sign', '0003_auto_20220126_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
