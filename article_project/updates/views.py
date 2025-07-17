from django.shortcuts import render,redirect,get_object_or_404
from articles.models import Article
from articles.forms import Article_Form

def update(request,id):
    article = get_object_or_404(Article,id=id)

    form = Article_Form(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    
    return render(request,'update.html',{'article':article,'form':form})

def delete(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    return redirect('article_list')