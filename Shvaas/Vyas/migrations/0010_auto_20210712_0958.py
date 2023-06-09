# Generated by Django 3.2 on 2021-07-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayurveda',
            name='herb_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='herb_description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='herb_image',
            field=models.ImageField(default='', upload_to='Vyas/images'),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='herb_link',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='herb_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='herb_strike_price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='herb_subcategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='use',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
