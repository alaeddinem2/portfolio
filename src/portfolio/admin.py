from django.contrib import admin
from . models import Project,Category,Client,ProjectImage,Contact
# Register your models here.


admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Contact)


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