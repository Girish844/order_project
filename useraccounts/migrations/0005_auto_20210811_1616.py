# Generated by Django 3.2.6 on 2021-08-11 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_architecture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architecture',
            old_name='dishes',
            new_name='restro1',
        ),
        migrations.RenameField(
            model_name='architecture',
            old_name='dishes_name',
            new_name='restro2',
        ),
        migrations.RenameField(
            model_name='architecture',
            old_name='dishes_price',
            new_name='restro3',
        ),
        migrations.RenameField(
            model_name='architecture',
            old_name='dishes_which_is_order',
            new_name='restro4',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='date',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='orderplaced',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='restaurant_address',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='restaurant_from_which_order_is_placed',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='restaurant_name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='restaurants',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='restaurants_in_which_dishes_are_avilable',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='user_who_placed_order',
        ),
    ]
