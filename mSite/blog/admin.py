from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date', 'published_date', 'count_text']
    list_display_links = ['title']

    def count_text(self, post):
        return '{}글자'.format(len(post.text))
    count_text.short_description = '글자수'


admin.site.register(Post, PostAdmin)
