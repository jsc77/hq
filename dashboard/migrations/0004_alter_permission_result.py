# Generated by Django 3.2 on 2021-05-31 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210531_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='result',
            field=models.IntegerField(default=3),
        ),
    ]
