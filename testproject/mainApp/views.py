from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
import json

from django.http import HttpResponse
from django.views import View
#from more.models import Podcast
#from .forms import PostForm, SearchForm
#from mainApp.forms import SearchForm
# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Send a demo:', 'sbnmuller@gmail.com']})

"""class Search(View):
    """ """Search all posts url: 127.0.0.1:8000/search/?q=<q>"""

"""def get(self, request):
        form = SearchForm()
        context = {'search': form}
        return render(request, 'search.html', context)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q']
            podcasts = Podcast.objects.filter(text__icontains=q)
            context = {'q': q, 'podcasts': podcasts}
            return_str = render_to_string('part_views/_post_search.html', context)
            return HttpResponse(json.dumps(return_str), content_type='application/json')
        else:
            HttpResponseRedirect("/search/")"""