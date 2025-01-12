from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Section, Course, Lesson, Comment
from .forms import CommentForm

def home(request):
    sections = Section.objects.all()
    return render(request, 'tutorials/home.html', {'sections': sections})

def section_detail(request, section_slug):
    section = get_object_or_404(Section, slug=section_slug)
    courses = section.courses.all().prefetch_related('lessons')
    total_lessons = sum(course.lessons.count() for course in courses)
    total_duration = section.total_duration()
    
    # Get the first preview lesson if available
    first_preview = None
    if courses:
        first_course = courses.first()
        if first_course:
            first_preview = first_course.lessons.filter(is_preview=True).first()
    
    context = {
        'section': section,
        'courses': courses,
        'total_lessons': total_lessons,
        'total_duration': total_duration,
        'what_youll_learn': section.get_what_youll_learn_list(),
        'requirements': section.get_requirements_list(),
        'first_preview': first_preview,
    }
    return render(request, 'tutorials/section_detail.html', context)

def course_detail(request, section_slug, course_slug):
    course = get_object_or_404(Course, section__slug=section_slug, slug=course_slug)
    lessons = course.lessons.all()
    current_lesson = lessons.filter(is_preview=True).first() or lessons.first()
    
    context = {
        'course': course,
        'lessons': lessons,
        'current_lesson': current_lesson,
    }
    return render(request, 'tutorials/course_detail.html', context)

def lesson_detail(request, section_slug, course_slug, lesson_slug):
    lesson = get_object_or_404(
        Lesson, 
        course__section__slug=section_slug,
        course__slug=course_slug,
        slug=lesson_slug
    )
    course = lesson.course
    lessons = course.lessons.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lesson = lesson
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('tutorials:lesson_detail', 
                          section_slug=section_slug,
                          course_slug=course_slug,
                          lesson_slug=lesson_slug)
    else:
        form = CommentForm()
    
    context = {
        'lesson': lesson,
        'course': course,
        'lessons': lessons,
        'form': form,
    }
    return render(request, 'tutorials/lesson_detail.html', context)

def pricing(request):
    return render(request, 'tutorials/pricing.html')
