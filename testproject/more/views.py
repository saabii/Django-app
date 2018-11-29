from django.shortcuts import render
from more.models import Podcast
from more.models import Author
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import View

# Create your views here.

class PodcastView(DetailView):
    model = Podcast
    template_name = 'more/mixes.html'
    context_object_name = 'podcast'


class ListView(View):
    model = Podcast
    template_name = "more/mixes.html"
    #objects.all().order_by("-publish_date")[:10]




class SearchView(View):
   template_name = 'search.html'
   def post(self, request, *args, **kwargs):
       data = request.POST['keyword']
       if data != '':
           result = {}
           result['podcasts'] = Podcast.objects.filter(Q(title__icontains=data) | Q(text__icontains=data))
           result['authors'] = Author.objects.filter(Q(name__icontains=data) | Q(id__icontains=data))
           return render(request, self.template_name, result)
       else:
           return redirect('/')

   def get(self, request, *args, **kwargs):
       return redirect('/')

"""class SearchView(View):
    template_name = 'search.html'

    def get(self,request,*args,**kwargs):
        query = self.request.GET.get(q)
        founded_podcasts = Podcast.objects.filter(Q(title_icontains-query)
             |Q (content_icontains-query))
        context ={
            'founded_podcasts': founded_podcasts
        }
        return render(self,request,self, template_name,context)"""


def index(reguest):
    return HttpResponse("<h3> Have a nice day!</h3>")
