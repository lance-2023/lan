# Generated by Django 4.2.1 on 2023-05-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_alter_customer__authentication"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="_authentication",
            field=models.JSONField(default=[]),
        ),
    ]
