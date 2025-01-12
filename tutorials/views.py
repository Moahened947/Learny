from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Section, Tutorial, Comment

class SectionListView(ListView):
    model = Section
    template_name = 'tutorials/home.html'
    context_object_name = 'sections'

class SectionDetailView(DetailView):
    model = Section
    template_name = 'tutorials/section_detail.html'
    context_object_name = 'section'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutorials'] = self.object.tutorials.all()
        return context

class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = 'tutorials/tutorial_detail.html'
    context_object_name = 'tutorial'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

def home(request):
    sections = Section.objects.all()
    return render(request, 'tutorials/home.html', {'sections': sections})

def pricing(request):
    return render(request, 'tutorials/pricing.html')

def add_comment(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            Comment.objects.create(
                tutorial=tutorial,
                author=author,
                content=content
            )
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Please fill in all fields.')
    return redirect('tutorials:tutorial_detail', pk=pk)
