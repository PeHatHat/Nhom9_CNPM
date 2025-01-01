from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Generates tokens for all existing users'

    def handle(self, *args, **options):
        User = get_user_model()
        for user in User.objects.all():
            token, created = Token.objects.get_or_create(user=user)
            print(f"Token for user {user.username}: {token.key}")