from django.urls import path
from .views import portfolio, project_details   

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<int:project_id>', project_details, name='project_details'),
]
