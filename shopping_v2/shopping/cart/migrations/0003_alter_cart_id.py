# Generated by Django 4.2.1 on 2023-06-05 01:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_alter_cart_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("c261a3bf-491c-44b2-8491-dc7bdd2f89f7"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
