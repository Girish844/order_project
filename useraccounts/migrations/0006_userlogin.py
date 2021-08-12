# Generated by Django 3.2.6 on 2021-08-11 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0005_auto_20210811_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.restaurants')),
            ],
        ),
    ]