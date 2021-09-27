from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
	path('',views.home),
	path('projects/<slug:slug>',views.project_detail, name='project_detail')
	
]