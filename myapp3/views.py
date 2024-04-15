# -*- coding: utf-8 -*-
from aiohttp.web_urldispatcher import View
from django.shortcuts import render, get_object_or_404
from .models import Author, Post
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse("Hello world from function")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello world from class!")


def year_post(request, year):
    text = ''
    ...
    return HttpResponse(f'Posts from {year} to {text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        ...
        return HttpResponse(f'Posts from {month}{year} <br> {text}')


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Pythonn работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': 'John'}
    return render(request, 'myapp3/index1.html', context)


class TempLIF(TemplateView):
    template_name = 'myapp3/index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello world'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/index3.html', context)


def my_view2(request):
    return render(request, 'myapp3/base.html')

def my_view3(request):
    return render(request, 'myapp3/index4.html')

def author_post(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author.html', {'author': author, 'posts': posts})


def author_post2(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post.html', {'post': post})


# Create your views here.
