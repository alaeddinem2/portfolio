from django import forms
from django.db.models import fields
from .models import Project

class NewProject(forms.ModelForm):
    class  Meta:
        model= Project
        fields= ('name','category','client','start_date','end_date','live_demo_url','github_url','image')
        