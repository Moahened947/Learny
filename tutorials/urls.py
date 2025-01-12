from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('<slug:section_slug>/', views.section_detail, name='section_detail'),
    path('<slug:section_slug>/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('<slug:section_slug>/<slug:course_slug>/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
]
