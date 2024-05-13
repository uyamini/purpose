from django.core.management.base import BaseCommand
from main_app.models import Post

class Command(BaseCommand):
    help = 'Populate the database with initial dummy data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Post.objects.all().delete()

        # Create dummy posts
        posts = [
            Post(
                location_state='California',
                location_city='Los Angeles',
                location_address='1234 Sunset Blvd',
                details='Family of four spotted near the park. Need food and blankets.',
                date_time_spotted='2024-05-12 08:30:00',
                list_of_needs='Food, Blankets, Water',
                status='need_help'
            ),
            Post(
                location_state='New York',
                location_city='New York City',
                location_address='5678 Broadway St',
                details='Individual spotted near the subway. Needs medical assistance and clothes.',
                date_time_spotted='2024-05-11 14:00:00',
                list_of_needs='Medical Assistance, Clothes',
                status='in_progress'
            ),
            Post(
                location_state='Illinois',
                location_city='Chicago',
                location_address='9101 Michigan Ave',
                details='Elderly person spotted near the library. Needs shelter and food.',
                date_time_spotted='2024-05-10 09:15:00',
                list_of_needs='Shelter, Food',
                status='helped'
            ),
        ]

        for post in posts:
            post.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data.'))
