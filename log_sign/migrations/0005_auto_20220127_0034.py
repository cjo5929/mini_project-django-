# Generated by Django 2.2.5 on 2022-01-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_sign', '0004_alter_user_first_name_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
