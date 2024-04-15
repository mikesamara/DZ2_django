from django.urls import path
from .views import hello, HelloView
from .views import my_view, view_for, my_view2, my_view3
from .views import year_post, MonthPost, post_detail
from .views import TempLIF
from .views import author_post, author_post2

urlpatterns = (
    path('hello/', hello, name='hello'),
    # path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    # path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('my_view/', my_view, name='my_view'),
    path('if/', TempLIF.as_view(), name='TempLIF'),
    path('view_for/', view_for, name='view_for'),
    path('my_view2/', my_view2, name='view_for'),
    path('my_view3/', my_view3, name='view_for'),
    path('my_view3/', my_view3, name='view_for'),
    path('author_post/<int:author_id>/', author_post, name='author_post'),
    path('author_post2/<int:post_id>/', author_post2, name='author_post2'),


)
