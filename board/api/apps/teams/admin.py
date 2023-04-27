from django.contrib import admin

from apps.teams.models import Column, ColumnLabel, Project, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('id', 'name')


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'name', 'team', 'color', 'created_at')
    search_fields = ('id', 'name', 'team')


@admin.register(ColumnLabel)
class ColumnLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'column', 'gitlab_label_id', 'created_at')
    search_fields = ('id', 'column', 'gitlab_label_id')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'gitlab_project_id', 'team', 'created_at')
    search_fields = ('id', 'gitlab_project_id', 'team')
