from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 저장되어있는 Article 들을 리스팅하는 페이지
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 사용자의 입력을 받아서 data를 전달하는 페이지
def new(request):
    return render(request, 'articles/new.html')

# 'new' 에서 받은 data를 Article 모델로 저장하는 페이지
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    context = {
        'title': title,
        'content': content,
    }
    return redirect('/articles/')

def delete(request, article_pk):
    # 특정 article 의 pk 값을 받아서 해당 article 삭제
    
    article = Article.objects.get(pk=article_pk)
    article.delete()
    
    # 삭제가 완료된 후 index 페이지로 돌려보낸다
    return redirect('/articles/')

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

