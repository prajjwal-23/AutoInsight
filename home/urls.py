from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cars', views.cars, name='cars'),
    path('bikes', views.bikes, name='bikes'),
    path('news', views.news, name='news'),
    path('news/<int:pk>/', views.detail_page, name='detail_page'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('termandcondition', views.termandcondition, name='termandcondition'),
    path('searchResult', views.searchResult, name='searchResult'),
    path('author', views.author, name='author'),
]
