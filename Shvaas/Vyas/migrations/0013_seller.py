# Generated by Django 3.2 on 2021-07-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0012_clothing_home_appliances_software_sports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('your_name', models.CharField(default='', max_length=50)),
                ('shop_name', models.CharField(default='', max_length=70)),
                ('your_phone', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=4000)),
                ('selling', models.CharField(default='', max_length=4000)),
            ],
        ),
    ]
