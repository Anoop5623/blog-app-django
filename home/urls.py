from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('postcomment', views.postcomment),
 # path('search',views.search),
  path('blog/<str:string>', views.blogdescription),
  path('', views.home, name="home" ),
  path('createblog',views.createblog),
  path('signup',views.signup),
  path('login',views.handlelogin),
  path('logout',views.handlelogout)
]