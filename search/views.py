from itertools import chain
from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from news.models import News
from structure.models import Branches, Specialists
from smi.models import smiArticles
from management.models import Management


class SearchView(ListView):
    template_name = 'search/index.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            news_results = News.objects.search(query)
            branches_results = Branches.objects.search(query)
            specialist_results = Specialists.objects.search(query)
            management_results = Management.objects.search(query)

            queryset_chain = chain(
                news_results,
                branches_results,
                specialist_results,
                management_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)
            return qs
        return News.objects.none()


