from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title # post.title이라는 컬럼을 title이라는 데이터에 넣는다.
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/posts/')

def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post, 
    }

    return render(request, 'edit.html', context)
    

def update(request, id):
    # 기존 정보 가져오기
    post = Post.objects.get(id=id)
    
    # 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존 정보를 새로운 정보로 바꾸기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')