from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.db.models import Q
#from django.models import Podcast


# надо придумать как сюда импортировать модели. джанго ругается из-за knowledge
# Create your views here.
class SearchView(View):
    template_name = 'search.html'

    def get(self,request,*args,**kwargs):
        query = self.request.GET.get(q)
        founded_podcasts = Podcast.objects.filter(Q(title_icontains-query)
             |Q (content_icontains-query))
        context ={
            'founded_podcasts': founded_podcasts
        }
        return render(self,request,self, template_name,context)



class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_podcast = Podcast.objects.filter(podcast_content__search=question)

            #Results = Podcast.objects.filter(author="sabina")
            #Podcast.objects.filter(name="sabina")

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_podcast, 10)

            page = request.GET.get('page')
            try:
                context['podcast_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['podcast_lists'] = current_page.page(1)
            except EmptyPage:
                context['podcast_lists'] = current_page.page(current_page.num_pages)

        return render_to_response(template_name=self.template_name, context=context)
