from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'created')
    list_filter = ['created']

admin.site.register(Project, ProjectAdmin)