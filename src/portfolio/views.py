from portfolio.models import Project
from django.shortcuts import render
from django.http.response import JsonResponse
from . models import Contact, Project, ProjectImage
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
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

def contact_page(request):
    return render(request,'portfolio/contact.html')

def contact_me(request):
    if request.method != "POST":
        return HttpResponse('Methode Not Allowed !')
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        try:
            contact=Contact(name=name,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,"Successfully sent message")
            return HttpResponseRedirect("/contact")
        except:
            messages.error(request, "Failed to send message")
            return HttpResponseRedirect("/contact")

        
        
    
    












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
    