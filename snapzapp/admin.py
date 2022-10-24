from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('post_id',)}
    list_filter = ('created_on', )
    list_display = ('description', 'slug', 'created_on')
    search_fields = ['description', ]
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment_text', 'post', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ['name', 'comment_text']
