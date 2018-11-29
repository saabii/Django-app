"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views
from more.models import Podcast

urlpatterns = [
    path('', ListView.as_view(queryset=Podcast.objects.all().order_by("-publish_date")[:10],template_name="more/mixes.html")),
    path('<int:pk>/', DetailView.as_view(model=Podcast, template_name="more/mix.html")),
    path('search/', views.SearchView.as_view(), name='search'),
]
