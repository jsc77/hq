# Generated by Django 3.2 on 2021-05-31 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_menuitem_video_url'),
        ('dashboard', '0006_alter_permission_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.ordermodel'),
        ),
    ]