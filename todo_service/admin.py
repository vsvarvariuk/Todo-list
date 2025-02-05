from django.contrib import admin

from todo_service.models import Tag, Task

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'datetime', 'is_done', 'deadline')
    list_filter = ('is_done', 'tags')
    search_fields = ('content',)

