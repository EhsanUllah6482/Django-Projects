from django.contrib import admin
from .models import Post, Author, Tag
# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'author', 'date', 'slug')
    search_fields = ('title', 'content')