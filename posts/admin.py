from django.contrib import admin

from .models import Post, Postfile


class PostFileInlineAdmin(admin.TabularInline):
    model = Postfile
    fields = ('file',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'is_active', 'created_time',)
    inlines = (PostFileInlineAdmin,)



