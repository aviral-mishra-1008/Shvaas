# Generated by Django 3.2 on 2021-07-23 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0023_auto_20210722_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='art_n_interior_designing',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='ayurveda',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='book',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='clothing',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='education',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='grocery',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='home_appliances',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='music',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='pch',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='product',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='software',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AddField(
            model_name='sports',
            name='path',
            field=models.CharField(default='', max_length=108),
        ),
    ]