from . import views
from django.urls import path
from django.views.generic import RedirectView

# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')

urlpatterns = [
    #Adding Redirect of home page to upload/
    path('', RedirectView.as_view(url='/upload')),
    path('upload/', views.upload_view, name='upload'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('annotate/<int:pk>/', views.annotate_view, name='annotate')
]
