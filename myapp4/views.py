# -*- coding: utf-8 -*-
from urllib import request

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import logging
from .models import Student

from .forms import ContactForm, ManyFieldsForm, ManyFieldsForm2, ImageForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp4/index.html')


def user_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}')
    else:
        form = ContactForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_forms(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp4/many_forms.html', {'form': form})


def many_forms_wiedget(request):
    if request.method == 'POST':
        form = ManyFieldsForm2(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}')
    else:
        form = ManyFieldsForm2()
    return render(request, 'myapp4/many_forms_wiedght.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}')
            new_user = Student(name=name, email=email, age=age)
            new_user.save()
            message = 'Пользователь сохранен'
    else:
        form = ContactForm()
        message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def image_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/image.html', {'form': form})

# Create your views here.
