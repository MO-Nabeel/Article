from django.shortcuts import render, redirect ,get_object_or_404
from .models import Article

def article_list(request):
    article = Article.objects.all()
    return render(request, 'article_list.html',{"art":article})

def article_create(request):
    try:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            author = request.POST['author']

            article = Article(title=title, content=content, author=author)
            article.save()
            return redirect('article_list')
    except:
        return redirect('article_list')

    return render(request,"article_form.html")

def article_detail(request,id):
    articles = get_object_or_404(Article,id=id)
    return render(request,"article_detail.html",{"article":articles})

