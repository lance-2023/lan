# Generated by Django 4.2.1 on 2023-05-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                ("_authentication", models.JSONField(default={})),
                ("company", models.CharField(default="", max_length=200)),
                ("first_name", models.CharField(default="", max_length=200)),
                ("last_name", models.CharField(default="", max_length=200)),
                ("phone", models.CharField(default="", max_length=200)),
                ("email", models.CharField(default="", max_length=200)),
                ("store_credit", models.IntegerField(default=0)),
                (
                    "registration_ip_address",
                    models.CharField(default="", max_length=200),
                ),
                ("customer_group_id", models.IntegerField(default=0)),
                ("notes", models.CharField(default="", max_length=200)),
                ("tax_exempt_category", models.CharField(default="", max_length=200)),
            ],
            options={
                "verbose_name": "customer",
                "verbose_name_plural": "customers",
                "db_table": "customer",
            },
        ),
    ]
