# Generated by Django 3.2 on 2021-06-04 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20210604_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images', width_field='width_field'),
        ),
    ]
