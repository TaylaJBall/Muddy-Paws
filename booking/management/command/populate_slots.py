from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from booking.models import Slot

class Command(BaseCommand):
    help = 'Populate booking slots for the next 6 days a week, excluding Sunday'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()

        # Define time slots for the day
        slot_times = [
            {'start': '10:00'},
            {'start': '12:00'},
            {'start': '14:00'},
            {'start': '16:00'}
        ]

        # Loop through the next 6 days, skipping Sunday
        current_date = today
        slots_created = 0

        for i in range(6):
            if current_date.weekday() == 6:
                current_date += timedelta(days=1)
                continue

            # Create 4 slots for each day
            for slot_time in slot_times:
                start_time_str = f"{current_date} {slot_time['start']}"

                start_time = timezone.make_aware(timezone.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M"))

                # Create the slot if it doesn't exist
                Slot.objects.get_or_create(start_time=start_time)

                slots_created += 1

            # Move to the next day
            current_date += timedelta(days=1)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {slots_created} slots.'))