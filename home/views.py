from django.shortcuts import render, get_object_or_404
from .models import Contact, News, Tag, Company, Category, Author
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    my_tag = Tag.objects.get(name='Latest News')
    my_tag_reviews = Tag.objects.get(name='Reviews')
    data = News.objects.all().filter(tags=my_tag).order_by('-id')[:3]
    data_reviews = News.objects.all().filter(tags=my_tag_reviews).order_by('-id')[:3]
    brands = Company.objects.all().order_by('-id')
    return render(request, 'index.html', {'data': data, 'data_reviews': data_reviews, 'brands': brands})


def detail_page(request, pk):
    detail = get_object_or_404(News, pk=pk)
    my_categoty = Category.objects.get(name='cars')
    data = News.objects.all().filter(category=my_categoty).order_by('-id')[:3]
    return render(request, 'detail_page.html', {'detail': detail, 'data': data})


def about(request):
    return render(request, 'about.html')


def termandcondition(request):
    return render(request, 'termandcondition.html')


def cars(request):
    my_categoty = Category.objects.get(name='cars')
    data = News.objects.all().filter(category=my_categoty).order_by('-id')
    paginator = Paginator(data,12)
    pageNumber = request.GET.get('page')
    datafinal = paginator.get_page(pageNumber)
    totalpage = datafinal.paginator.num_pages
    return render(request, 'cars.html', {'data': datafinal, 'lastpage': totalpage, 'pagelist':[n+1 for n in range (totalpage)]})


def bikes(request):
    my_categoty = Category.objects.get(name='bikes')
    data = News.objects.all().filter(category=my_categoty).order_by('-id')
    paginator = Paginator(data,12)
    pageNumber = request.GET.get('page')
    datafinal = paginator.get_page(pageNumber)
    totalpage = datafinal.paginator.num_pages
    return render(request, 'bikes.html', {'data': datafinal, 'lastpage': totalpage, 'pagelist':[n+1 for n in range (totalpage)]})


def news(request):
    data = News.objects.prefetch_related('tags').all().order_by('-id')
    paginator = Paginator(data,12)
    pageNumber = request.GET.get('page')
    datafinal = paginator.get_page(pageNumber)
    totalpage = datafinal.paginator.num_pages
    return render(request, 'news.html', {'data': datafinal, 'lastpage': totalpage, 'pagelist':[n+1 for n in range (totalpage)]})


def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message sent successfully.')
    return render(request, 'contact.html')


def searchResult(request):
    query = request.GET.get('query', '')
    result = News.objects.filter(Q(title__icontains=query) |
        Q(category__name__icontains=query) |
        Q(companies__name__icontains=query) |
        Q(author__name__icontains=query) |
        Q(tags__name__icontains=query)).distinct().order_by('-id')
    paginator = Paginator(result,9)
    pageNumber = request.GET.get('page')
    datafinal = paginator.get_page(pageNumber)
    totalpage = datafinal.paginator.num_pages
    return render(request, 'searchResult.html', {'data': datafinal, 'query': query, 'lastpage': totalpage, 'pagelist':[n+1 for n in range (totalpage)]})

def author(request):
    authorData = Author.objects.all()
    query = request.GET.get('query', '')
    result = News.objects.filter(Q(title__icontains=query) |
        Q(category__name__icontains=query) |
        Q(companies__name__icontains=query) |
        Q(author__name__icontains=query) |
        Q(tags__name__icontains=query)).distinct().order_by('-id')
    paginator = Paginator(result,9)
    pageNumber = request.GET.get('page')
    datafinal = paginator.get_page(pageNumber)
    totalpage = datafinal.paginator.num_pages
    return render(request, 'author.html', {'authorData': authorData, 'data': datafinal, 'query': query, 'lastpage': totalpage, 'pagelist':[n+1 for n in range (totalpage)]})