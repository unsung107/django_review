# Django review

## 시작하기

```bash
$ venv
$ python -m venv venv #가상환경을 만든다 - 프로젝트마다 사용하는 모듈이 달라질 수 있기때문에

```



후에 Ctrl + Shift + P => python interpreter => python 3.74 (venv: venv)로 설정

### settings.json

```json
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {"django-html": "html"},
    "[djagno-html]":{
        "editor.tabSize": 2,
    },
}
```

을 설정해준다.

## 프로젝트 시작

```bash
$ django-admin startproject django_review .
```

로켓트 띄우기

```bash
$ python manage.py runserver
```

## 어플리케이션 만들기



```bash
$ python manage.py startapp pages
```

어플리 케이션을 만들고 꼭!! 출생신고를 해야한다

### settings.py

```python
INSTALLED_APPS = [
    # Local apps
    'pages',
```



어떤 요청이와도 django_review/urls.py 로 먼저간다.

### django_review/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]


```

pages/ 로 들어오는 모든 요청을 pages/urls.py에서 확인한다

하지만 지금 pages/urls.py 가 없기때문에 새로 만들어준다. 이때 반드시! 

urlpatterns = [] 리스트가 있어야한다.

### pages/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from . import views #현재 디렉토리에서 views 를가져온다.

#domain.com/pages/____
urlpatterns = [
    path('/', views.index)
]

```



## models!

### articles/models.py

```python
from django.db import models

# Create your models here.

class Article(models.Model): #쟝고의 모델을 상속해온다
    title = models.CharField(max_length=20) #맥스랭스는 필수인자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

그 후에 터미널에서

```bash
$ python manage.py makemigrations
```

로 모델을 만든것을 알려준다

articles/migrations에 파일이 생성된다. => 실제 DB 반영할 준비 끝

```bash
$ python manage.py migrate
```

### article/views.py

```python

from .models import Article

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = ()
    article.title = title
    article.content = content
    article.save()
    
    context = {
        'title': title,
        'content': content,
    }
    return render(request, 'articles/create.html', context)
```

임포트를 통해 Article 모델을 불러오고

불러와 저장해준다.



## Index 에서 저장되어있는 DB를 리스트화 해보자!

```python
# 저장되어있는 Article 들을 리스팅하는 페이지
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

Article 에 있는 모든 오브젝트를 불러와 저장한다.

### articles/index.html

```html
    <h1>Hello</h1>
    <a href="/articles/new/">[게시글작성]</a>
    <hr>
    {% for article in articles %}
    <article>
      <h4>{{ article.pk}} {{ article.title }}</h4>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      
    </article>
    <hr>
    {% endfor %}
```



## 삭제하기

### articles/views.py

```python
from django.shortcuts import render, redirect

def delete(request, article_pk):
    # 특정 article 의 pk 값을 받아서 해당 article 삭제
    
    article = Article.objects.get(pk=article_pk)
    article.delete()
    
    # 삭제가 완료된 후 index 페이지로 돌려보낸다
    return redirect('/articles/')
```

삭제 후 굳이 새로운 페이지를 만들어줄 필요가 없다.

이럴땐 redirect를 사용하여 인덱스로 돌려준다!



## 수정하기

### views.py

```python
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article.objects.get(pk=article_pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('/articles/')
```

마찬가지로 update는 굳이 만들어줄필요가 없이 redirect로 한다

### edit.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>New Article</title>
</head>
<body>
    <h1>게시글 수정</h1>
    <form action="/articles/{{ article.pk }}/update/">
      <input type="text" name="title" value="{{article.title}}"><br>
      <textarea name="content" id="" cols="30" rows="10">{{ article.content }}</textarea><br>
      <button type="submit">수정하기</button><br>
      <a href="/articles/">뒤로가기</a>
    </form>

</body>
</html>
```

