# Generated by Django 3.2.2 on 2021-05-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swapindex',
            fields=[
                ('entryId', models.AutoField(primary_key=True, serialize=False)),
                ('courseCode', models.CharField(max_length=60)),
                ('currentIndex', models.IntegerField()),
                ('wantIndex', models.IntegerField()),
                ('username', models.CharField(max_length=60)),
                ('chatId', models.IntegerField()),
            ],
        ),
    ]
