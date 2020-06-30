from django.contrib import admin
from .models import Destinations, Comment, Contact

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Contact)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Destinations)
