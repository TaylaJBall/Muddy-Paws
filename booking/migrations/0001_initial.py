# Generated by Django 4.2.16 on 2024-11-29 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                (
                    "service_type",
                    models.CharField(
                        choices=[
                            ("PAMPER_PACKAGE", "Pamper Package"),
                            ("FULL_GROOM", "Full Groom"),
                            ("HAND_STRIP", "Hand Strip"),
                        ],
                        default="PAMPER_PACKAGE",
                        max_length=50,
                    ),
                ),
                ("booking_date", models.DateField()),
                ("booking_time", models.TimeField()),
                ("approved", models.BooleanField(default=False)),
                ("notes", models.TextField(max_length=500)),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_pet",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-booking_date", "-booking_time"],
            },
        ),
    ]
