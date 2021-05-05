from wall.models import Post

class Feed:
    '''Service feeds'''
    def get_post_list(self, user):
        return Post.objects.filter(user__owner__subscriber=user).order_by('-create_date')\
            .select_related('user').prefetch_related('comments')

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').prefetch_related('comments').get(id=pk)

feed_service = Feed()