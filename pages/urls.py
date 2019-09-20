from django.contrib import admin
from django.urls import path, include
from . import views

# domain.com/pages/____ (/까지 포함된 경로이다. 그럼 pages//가 되지않을까?! 그래서 '' 빈스트링을 넣어준다)
urlpatterns = [
    path('', views.index),
    path('greeting/<str:name>', views.greeting),
]
