# Generated by Django 2.1.2 on 2018-11-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181124_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
