from portfolio.models import Project
from django.shortcuts import render
from django.http.response import JsonResponse
from . models import Contact, Project, ProjectImage, Visit
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from invitations.utils import get_invitation_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def get_ip(request):
    
    try:
         x_forward=request.META.get("HTTP_X_FORWARDED_FOR")
         if x_forward:
            ip=x_forward.split(",")[0]
         else:
            ip=request.META.get("REMOTE_ADDR")
    except:
            ip="none"
    
    return ip

def home(request):
    if request.user.is_authenticated:
        ip=get_ip(request)
            
        username=None
        username = request.user.username
        
        print(username)
        visit=Visit(visitor_ip=ip,visitor_name=username)
        visit.save()
    else:
        pass

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
      
    
def contact_me(request) :

     if request.method != "POST":
            return HttpResponse('Methode Not Allowed !')
         
     else:
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
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
    