# Generated by Django 2.2.5 on 2020-12-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20201212_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swapindex',
            name='available',
        ),
        migrations.AlterField(
            model_name='swapindex',
            name='courseCode',
            field=models.CharField(max_length=60),
        ),
    ]
