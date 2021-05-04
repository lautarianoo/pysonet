from django.core.management.base import BaseCommand
from profiles.models import UserNet
from followers.models import Follower
from wall.models import Post

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout.write('Success')

    def create_user(self):
        for i in range(10):
            user = UserNet.objects.create(username=f"test{i+2}", email=f"test{i}@gmail.com",
                                   is_active=True, middle_name=f"test{i}", phone=f"12345678910{i}",
                                   gender=1)
            user.set_password('fdhgrehg')
            user.save()

    def create_follower(self):
        user_list = UserNet.objects.all().order_by()[2:]
        for user in user_list:
            Follower.objects.create(user=user, subscriber_id=1)

    def create_post(self):
        user_list = UserNet.objects.all()
        for user in user_list:
            for _ in range(10):
                Post.objects.create(text=f'Test Post {_}', user=user)