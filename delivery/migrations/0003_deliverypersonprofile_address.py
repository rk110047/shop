# Generated by Django 2.1.5 on 2020-07-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20200705_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverypersonprofile',
            name='address',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]