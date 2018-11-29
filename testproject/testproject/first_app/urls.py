from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
