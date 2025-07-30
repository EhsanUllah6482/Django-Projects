from django.contrib import admin
from .models import Post, Author, Tag,Comment
# Register your models here.



class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'post', 'text')
    search_fields = ('user_name', 'user_email', 'text')
    list_filter = ('post',)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'author', 'date', 'slug')
    search_fields = ('title', 'content')



admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)