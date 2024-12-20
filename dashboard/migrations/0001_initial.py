# Generated by Django 4.2.16 on 2024-11-29 13:52

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
            name="Pet",
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
                ("pet", models.CharField(max_length=50)),
                ("breed", models.CharField(max_length=50)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        default="male",
                        max_length=50,
                    ),
                ),
                ("colour", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("allergies", models.BooleanField(default=False)),
                ("vaccinated", models.BooleanField(default=False)),
                ("microchipped", models.BooleanField(default=False)),
                ("spayed_neutered", models.BooleanField(default=False)),
                ("extra_info", models.TextField(max_length=300)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
