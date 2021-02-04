from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, App
from .forms import CommentForm 
from .models import Comment


def home(request):
    context = {
        "apps": App.objects.filter(status = 'n').order_by('-created'),
    }
    return render(request, "apps/index.html", context)

def AppDetail(request, slug):
    if request.method == 'POST': 
        cf = CommentForm(request.POST or None) 
        if cf.is_valid(): 
            content = request.POST.get('content') 
            post=get_object_or_404(App, slug = slug)
            comment = Comment.objects.create(post = post, user = request.user, content = content) 
            comment.save() 
            return redirect(post.get_absolute_url()) 
    else: 
      cf = CommentForm() 
        
    context = {
        "app": get_object_or_404(App, slug = slug),
        'comment_form':cf,
    }
    return render(request, "apps/app_detail.html", context)

def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug = slug),
    }
    return render(request, "apps/category.html", context)



