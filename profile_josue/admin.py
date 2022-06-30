from django.contrib import admin
from .models import HomeProfile

# Register your models here.
class HomeProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'description')

admin.site.register(HomeProfile, HomeProfileAdmin)