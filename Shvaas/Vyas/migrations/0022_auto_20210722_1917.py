# Generated by Django 3.2 on 2021-07-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0021_alter_orders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=111),
        ),
    ]
