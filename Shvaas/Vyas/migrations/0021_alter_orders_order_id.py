# Generated by Django 3.2 on 2021-07-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0020_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='', max_length=25),
        ),
    ]
