from django.contrib import admin
from .models import Project, Task




class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'deadline', 'end_date')
    search_fields = ('name', 'location__name')
    list_filter = ('location',)
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'start_date', 'deadline', 'end_date')
    search_fields = ('name', 'project__name')
    list_filter = ('project',)