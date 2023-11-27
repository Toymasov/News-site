from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm


# Create your views here.

def news_list(request):
    #news_list = News.objects.filter(status=News.Status.Published)

    news_list = News.published.all()
    context = {
        'news_list': news_list
    }

    return render(request, 'news/news_list.html', context)
def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }

    return render(request, 'news/news_detail.html', context)
def HomePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:5]
    local_list = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[:5]
    world_list = News.published.all().filter(category__name='Dunyo').order_by('-publish_time')[:5]
    futbol_list = News.published.all().filter(category__name='Futbol').order_by('-publish_time')[:5]
    boks_list = News.published.all().filter(category__name='Boks').order_by('-publish_time')[:5]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_list': local_list,
        'world_list': world_list,
        'futbol_list': futbol_list,
        'boks_list': boks_list,
    }

    return render(request, 'news/home.html', context)


# def contactPageView(request):
#     #print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse('<h2> Biz bilan bog‘langaningiz uchun tashakkur </h2')
#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)

class contactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2>Biz bilan bog`langaningiz uchun rahmat</h2>')
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)
def fzfPageView(request):
    context = {

    }

    return render(request, 'news/404.html', context)

class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news

class WorldNewsView(ListView):
    model = News
    template_name = 'news/world.html'
    context_object_name = 'world_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Dunyo')
        return news

class FutbolNewsView(ListView):
    model = News
    template_name = 'news/futbol.html'
    context_object_name = 'futbol_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Futbol')
        return news

class BoksNewsView(ListView):
    model = News
    template_name = 'news/boks.html'
    context_object_name = 'boks_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Boks')
        return news