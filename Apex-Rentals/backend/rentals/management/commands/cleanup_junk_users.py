from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Deletes users who joined >7 days ago and are NOT verified'

    def handle(self, *args, **kwargs):
        # 1. Define the cutoff date (7 days ago)
        cutoff_date = timezone.now() - timedelta(days=7)
        
        # 2. Find unverified users joined before that date
        # We exclude 'is_staff' so we don't accidentally delete Admins!
        junk_users = User.objects.filter(
            date_joined__lt=cutoff_date, 
            profile__is_verified=False,
            is_staff=False 
        )

        count = junk_users.count()
        
        if count > 0:
            junk_users.delete()
            self.stdout.write(self.style.SUCCESS(f"Successfully deleted {count} junk users."))
        else:
            self.stdout.write(self.style.SUCCESS("No junk users found."))