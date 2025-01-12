from django.contrib import admin
from .models import Section, Course, Lesson, Comment

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class CourseInline(admin.StackedInline):
    model = Course
    extra = 1

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'created_at', 'updated_at')
    list_filter = ('level', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CourseInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'created_at')
    list_filter = ('section', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LessonInline]
    list_editable = ['order']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration', 'is_preview', 'order', 'created_at')
    list_filter = ('course', 'is_preview', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_preview']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'lesson', 'created_at')
    list_filter = ('created_at', 'lesson')
    search_fields = ('author', 'content')
