from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('section/<int:pk>/', views.SectionDetailView.as_view(), name='section_detail'),
    path('tutorial/<int:pk>/', views.TutorialDetailView.as_view(), name='tutorial_detail'),
    path('tutorial/<int:pk>/comment/', views.add_comment, name='add_comment'),
]
