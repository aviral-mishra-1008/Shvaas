# Generated by Django 3.2 on 2021-07-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0022_auto_20210722_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
    ]
