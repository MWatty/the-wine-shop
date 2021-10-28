from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image_url',
        'datetime',
    )

    ordering = ('name',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = (
        'blog',
        'user_profile',
        'datetime',
    )
    list_display = (
        'blog',
        'user_profile',
        'description',
        'datetime',
        )

    ordering = ('blog',)


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
