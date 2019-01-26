# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models

def index(request):
    # return HttpResponse('hello world')
    # return render(request,'index.html',{'hello': })

    # 注意这里的objects 要加s
    # article = models.Article.objects.get(pk=2)
    # 获取所有参数
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles': articles})

# 文章列表页面
def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

# 编写提交新的文章  或者编写旧的文章
def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

# 提交新文章后返回的页面
def edit_action(request):
    title = request.POST.get('title','TETLE')
    content = request.POST.get('content','CONTENT')

    article_id = request.POST.get('article_id',0)

    if article_id == '0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request,'blog/index.html',{'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})

