# Generated by Django 4.1.5 on 2023-01-10 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_customer_verification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='verification',
            new_name='verification_token',
        ),
    ]
