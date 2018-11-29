from django.contrib import admin
from more.models import Podcast
from more.models import Author
from more.models import Genre

# Register your models here.
admin.site.register(Podcast)
admin.site.register(Author)
admin.site.register(Genre)

