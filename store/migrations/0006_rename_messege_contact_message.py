# Generated by Django 4.1.3 on 2022-12-23 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_whatsapp_no_contact_whatsapp_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messege',
            new_name='message',
        ),
    ]