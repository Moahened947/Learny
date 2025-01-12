from django.contrib import admin
from .models import Section, Tutorial

# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'section__title')
    list_filter = ('section', 'created_at', 'updated_at')
