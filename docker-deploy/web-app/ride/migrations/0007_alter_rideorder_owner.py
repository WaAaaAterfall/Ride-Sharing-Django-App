# Generated by Django 4.1.5 on 2023-02-02 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ride', '0006_remove_driver_comment_remove_driver_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rideorder',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]