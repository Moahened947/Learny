from django.db import models
from django.core.exceptions import ValidationError

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
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='sections/thumbnails/', 
                                validators=[validate_image_extension],
                                help_text='Upload a section thumbnail (16:9 ratio recommended)',
                                null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

class Tutorial(models.Model):
    section = models.ForeignKey(Section, related_name='tutorials', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='tutorials/videos/', validators=[validate_video_extension])
    thumbnail = models.ImageField(upload_to='tutorials/thumbnails/', validators=[validate_image_extension], 
                                help_text='Upload a thumbnail image (16:9 ratio recommended)',
                                null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

class Comment(models.Model):
    tutorial = models.ForeignKey(Tutorial, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.tutorial.title}'

    class Meta:
        ordering = ['-created_at']
