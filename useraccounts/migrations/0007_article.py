# Generated by Django 3.2.6 on 2021-08-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0006_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restro1', models.CharField(max_length=100)),
                ('restro2', models.CharField(max_length=100)),
                ('restro3', models.CharField(max_length=100)),
                ('restro4', models.CharField(max_length=100)),
            ],
        ),
    ]
