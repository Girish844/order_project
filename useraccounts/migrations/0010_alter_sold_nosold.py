# Generated by Django 3.2.6 on 2021-08-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0009_rename_sold_sold_nosold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='nosold',
            field=models.IntegerField(),
        ),
    ]