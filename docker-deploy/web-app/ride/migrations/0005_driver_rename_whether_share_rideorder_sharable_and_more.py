# Generated by Django 4.1.5 on 2023-02-01 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ride', '0004_rename_owner_rideorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Car', max_length=50)),
                ('plate', models.CharField(default='000', max_length=50)),
                ('capacity', models.IntegerField(default=4)),
                ('comment', models.CharField(default='000', max_length=100)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='rideorder',
            old_name='whether_share',
            new_name='sharable',
        ),
        migrations.AddField(
            model_name='rideorder',
            name='remaining_passenger_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rideorder',
            name='owner',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]