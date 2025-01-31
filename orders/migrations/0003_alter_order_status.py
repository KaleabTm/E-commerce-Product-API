# Generated by Django 5.1.4 on 2025-01-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_rename_total_price_orderitem_item_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("APPROVED", "Approved"),
                    ("CANCELLED", "Cancelled"),
                    ("DELIVERED", "Delivered"),
                ],
                default="PENDING",
                max_length=15,
            ),
        ),
    ]
