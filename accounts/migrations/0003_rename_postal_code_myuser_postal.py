# Generated by Django 4.2 on 2024-08-15 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_myuser_delete_customuser"),
    ]

    operations = [
        migrations.RenameField(
            model_name="myuser",
            old_name="postal_code",
            new_name="postal",
        ),
    ]
