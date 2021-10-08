from django.contrib import admin
from . models import Project,Category,Client,ProjectImage,Contact, Visit
# Register your models here.


admin.site.register(Client)
admin.site.register(Category)



class VisitorAdmin(admin.ModelAdmin):
    
    list_display = ('id','visitor_name','visitor_ip','time')
    list_filter = ('id','visitor_name','visitor_ip','time')
admin.site.register(Visit,VisitorAdmin)






class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
       model = Project
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('name','email','subject','message')
    list_filter = ('name','email','subject','message')
    #list_editable = ('name','email','subject','message')
    

admin.site.register(Contact,ContactAdmin)