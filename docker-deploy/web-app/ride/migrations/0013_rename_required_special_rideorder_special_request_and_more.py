# Generated by Django 4.1.5 on 2023-02-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0012_rename_vtype_drivervehicle_vehicle_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rideorder',
            old_name='required_special',
            new_name='special_request',
        ),
        migrations.RemoveField(
            model_name='drivervehicle',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='rideorder',
            name='driver_name',
        ),
        migrations.RemoveField(
            model_name='rideorder',
            name='driver_plate',
        ),
        migrations.RemoveField(
            model_name='rideorder',
            name='max_share_num',
        ),
        migrations.RemoveField(
            model_name='rideorder',
            name='remaining_passenger_num',
        ),
        migrations.RemoveField(
            model_name='rideorder',
            name='sharer_num',
        ),
        migrations.AddField(
            model_name='rideorder',
            name='driver_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]
