# Generated by Django 3.2 on 2021-06-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_auto_20210614_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]