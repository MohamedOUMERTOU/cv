# mycv/admin.py

from django.contrib import admin
from .models import Project ,Exprience,Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Exprience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'startDate', 'endDate', 'profil','adress')

@admin.register(Skill)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'icon')