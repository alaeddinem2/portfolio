from portfolio.models import Project
from django.shortcuts import render
from django.http.response import JsonResponse
from . models import Project, ProjectImage
# Create your views here.
def home(request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }
    return render(request,'portfolio/home.html',context)

def project_detail(request,slug):
    project=Project.objects.get(slug=slug)
    images=ProjectImage.objects.filter(project=project)
    context={
        
        'project':project,
        'images':images
    }
    return render(request,'portfolio/project_detail.html',context)
    












# def home(request):
#     About=[
#         {
#             'birthday':'13 february 1992',
#             'website':'www.telliala.com',
#             'phone':'+213664661955',
#             'country':'Algeria',
#             'Age':'29',
#             'degree':'Master',
#             'email':'telliala@gmail.com',
#             'freelancer':'Available'
#         }
#     ]
#     return JsonResponse (About, safe=False)
    