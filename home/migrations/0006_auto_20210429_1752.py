# Generated by Django 3.1.7 on 2021-04-29 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.client'),
        ),
    ]
