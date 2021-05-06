# Generated by Django 3.1.7 on 2021-05-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210503_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='post',
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.messagemodel'),
        ),
    ]
