# Generated by Django 3.2 on 2021-06-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_ordermodel_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='contract_images/')),
            ],
        ),
    ]