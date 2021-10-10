from typing import Pattern
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
	path('',views.home,name="home"),
	path('projects/<slug:slug>',views.project_detail, name='project_detail'),
	path('contact',views.contact_page,name="contact"),
	path('contact_me',views.contact_me,name="contact_me_save"),
	path('create_project',views.create_project,name="create_project"),
	
]