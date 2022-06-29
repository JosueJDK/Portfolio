from django.shortcuts import render
from .models import HomeProfile
# Create your views here.
def home(request):
    home_profile = HomeProfile.objects.all()
    return render(request, 'home.html', {'home_profile': home_profile})

def profile(request):
    return render(request, 'profile.html')