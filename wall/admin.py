from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from wall.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_date', 'published', 'moderation', 'view_count', 'id')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_date', 'update_date', 'published', 'id')
    mptt_level_indent = 15
