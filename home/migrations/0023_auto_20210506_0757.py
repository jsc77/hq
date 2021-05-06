# Generated by Django 3.2 on 2021-05-05 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20210504_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ordered',
            new_name='is_ordered',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='ordered',
            new_name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AddField(
            model_name='client',
            name='items',
            field=models.ManyToManyField(blank=True, to='home.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.client'),
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_ordered',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.item'),
        ),
    ]
