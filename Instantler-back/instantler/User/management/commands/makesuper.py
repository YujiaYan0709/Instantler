from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="yansky").exists():
            User.objects.create_superuser("yansky", "yanyujia0709@163.com", "Yanyujia0709")
