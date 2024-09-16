from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                    # Home page
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio page listing all projects
    path('project/<int:id>/', views.project_detail, name='project_detail'),  # Detail page for a specific project
    path('contact/', views.contact, name='contact'),        # Contact page
]
