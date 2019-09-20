from django.contrib import admin
from django.urls import path, include
from . import views

# domain.com/pages/____ (/까지 포함된 경로이다. 그럼 pages//가 되지않을까?! 그래서 '' 빈스트링을 넣어준다)
urlpatterns = [
    path('<int:article_pk>/update/', views.update),
    path('<int:article_pk>/edit/', views.edit),
    path('<int:article_pk>/delete/', views.delete),
    path('create/', views.create),
    path('', views.index),
    path('new/', views.new),
]
