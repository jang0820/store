# Generated by Django 4.2 on 2024-08-18 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_remove_order_order_order_createt_7ef041_idx_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["-createtime"],
                "permissions": (
                    ("order_delete", "Can Delete Order"),
                    ("order_create", "Can Create Order"),
                    ("order_update", "Can Update Order"),
                ),
            },
        ),
    ]
