# Generated by Django 3.2 on 2021-07-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0024_auto_20210723_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayurveda',
            name='path',
            field=models.CharField(default='/Vyas/ayurveda/', max_length=108),
        ),
    ]
