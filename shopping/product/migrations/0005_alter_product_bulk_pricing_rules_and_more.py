# Generated by Django 4.2.1 on 2023-05-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_product_bulk_pricing_rules_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="bulk_pricing_rules",
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name="product",
            name="custom_fields",
            field=models.JSONField(default={}),
        ),
    ]
