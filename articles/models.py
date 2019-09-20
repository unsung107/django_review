from django.db import models

# Create your models here.

class Article(models.Model): #쟝고의 모델을 상속해온다
    title = models.CharField(max_length=20) #맥스랭스는 필수인자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)