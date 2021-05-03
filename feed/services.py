from wall.models import Post
from followers.models import Follower

def feed(user):
    #1

    news = []
    subscribe = Follower.objects.filter(subscriber=user)
    for sub in subscribe:
        news.append(Post.objects.filter(user=sub.user, create_date__hour=1).order_by('-create_date'))

    #2

