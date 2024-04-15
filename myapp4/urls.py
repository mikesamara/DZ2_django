from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/add/', views.user_form, name='user_form'),
    path('forms/', views.many_forms, name='many_forms'),
    path('wiedht/', views.many_forms_wiedget, name='many_forms_wiedget'),
    path('add_user/', views.add_user, name='add_user'),
    path('image_form/', views.image_form, name='image_form')


]