# Generated by Django 4.2.1 on 2023-06-01 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0006_alter_customer__authentication"),
        ("order", "0003_remove_order_consignments_remove_order_is_deleted_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="customer_id",
        ),
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="customer.customer",
            ),
        ),
    ]
