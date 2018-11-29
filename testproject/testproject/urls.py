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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#from django.conf.urls import url, include
from django.conf.urls import url
#from .core import views as s
from django.views.generic import TemplateView
#from testproject.more.views import SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('first_app/', include('first_app.urls')),
    path('more/', include('more.urls')),
    # url: 127.0.0.1:8000/search/?q=<q>
    #path('', 'search/', Search.as_view()),
    #path('search/', include('search.urls')),
    #path('signup/', s.signup, name='signup'),
    #path('',search, SearchView.as_view(),name='search_view')
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






