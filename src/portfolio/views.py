from portfolio.models import Project
from django.shortcuts import render
from django.http.response import JsonResponse
from . models import Contact, Project, ProjectImage, Visit
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from datetime import datetime
from django.utils import timezone
from threading import Timer
from ipware import get_client_ip


# get ip user and save it in database
def save_ip(request):
   # if request.user.is_authenticated:
        ip=get_client_ip(request)
        ip=ip[0]
        print(ip)
        time=timezone.now().strftime("%Y-%m-%d "   " %H:%M:%S")
        visit=Visit(visitor_ip=ip,visitor_name=request.user,time=time)
        visit.save()
        
    


def home(request):
    
    #call the function when get home page
    save_ip(request)   
     
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
    