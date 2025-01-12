from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

def validate_video_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file format. Please use MP4, AVI, MOV, or MKV.')

def validate_image_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file format. Please use JPG, JPEG, PNG, or WEBP.')

class Section(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='sections/thumbnails/', 
                                validators=[validate_image_extension],
                                help_text='Upload a section thumbnail (16:9 ratio recommended)',
                                null=True, blank=True)
    what_youll_learn = models.TextField(help_text='Enter each point on a new line')
    requirements = models.TextField(help_text='Enter each requirement on a new line', blank=True)
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('all', 'All Levels')
    ], default='all')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def total_duration(self):
        total = 0
        for course in self.courses.all():
            for lesson in course.lessons.all():
                total += lesson.duration
        return total

    def get_what_youll_learn_list(self):
        return [x.strip() for x in self.what_youll_learn.split('\n') if x.strip()]

    def get_requirements_list(self):
        return [x.strip() for x in self.requirements.split('\n') if x.strip()]

    class Meta:
        ordering = ['-created_at']

class Course(models.Model):
    section = models.ForeignKey(Section, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def total_duration(self):
        return sum(lesson.duration for lesson in self.lessons.all())

    class Meta:
        ordering = ['order', 'created_at']
        unique_together = ['section', 'slug']

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='lessons/videos/', validators=[validate_video_extension])
    thumbnail = models.ImageField(upload_to='lessons/thumbnails/', 
                                validators=[validate_image_extension],
                                help_text='Upload a thumbnail image (16:9 ratio recommended)',
                                null=True, blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in seconds')
    is_preview = models.BooleanField(default=False, help_text='Is this a preview lesson?')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def format_duration(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"

    class Meta:
        ordering = ['order', 'created_at']
        unique_together = ['course', 'slug']

class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.lesson.title}"

    class Meta:
        ordering = ['-created_at']
