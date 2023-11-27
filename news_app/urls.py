from django.urls import path
from .views import news_list, news_detail, HomePageView, contactPageView, fzfPageView, LocalNewsView, WorldNewsView, FutbolNewsView, BoksNewsView

urlpatterns = [
    path('', HomePageView, name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', contactPageView.as_view(), name='contact_page'),
    path('fzf/', fzfPageView, name='404_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('world/', WorldNewsView.as_view(), name='world_news_page'),
    path('futbol/', FutbolNewsView.as_view(), name='futbol_news_page'),
    path('boks/', BoksNewsView.as_view(), name='boks_news_page'),
]