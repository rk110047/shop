# Generated by Django 2.1.5 on 2020-06-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200609_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='middle_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
