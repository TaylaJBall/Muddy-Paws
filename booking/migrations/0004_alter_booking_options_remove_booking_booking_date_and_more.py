# Generated by Django 4.2.16 on 2024-12-03 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_slot_rename_approved_booking_slotapproved_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"ordering": ["-slot"]},
        ),
        migrations.RemoveField(
            model_name="booking",
            name="booking_date",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="booking_time",
        ),
    ]