from django.contrib import admin

from blogapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title',)
    list_filter = ('author',)
    # list_editable = ('author',)

admin.site.register(Post, PostAdmin)