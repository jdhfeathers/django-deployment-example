from django.urls import path, re_path, include
from basic_app import views

app_name='basic_app'

urlpatterns=[
    re_path(r'^page1/$', views.page1,name='page1'),
    re_path(r'^another/$', views.another, name='another'),
    re_path(r'^user/$',views.user, name='user'),

]