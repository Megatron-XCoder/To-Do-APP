from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import TodoItem, Tag

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'description', 'status', 'due_date', 'tags'),
        }),
        ('Timestamps', {
            'fields': ('timestamp',),
        }),
    )
    readonly_fields = ('timestamp',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
