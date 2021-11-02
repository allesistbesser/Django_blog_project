from django.shortcuts import render , redirect , get_object_or_404
from .models import Post , Like , Comment
from .forms import PostForm
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post(request):
    posts = Post.objects.all()
    likes = Like.objects.values('post').annotate(count=Count('post'))
    comments = Comment.objects.values('post').annotate(count=Count('post'))
      
    context = {
       'posts': posts,
       'likes': likes,
       'comments': comments,
    }
    return render( request, 'blog/post.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments=Comment.objects.all()
    like = Like.objects.all().filter(post=id).count()
    is_like = Like.objects.filter(user=request.user, post=post)
    
    context = {
        'post':post,
        'comments': comments,
        'like': like,
        'is_like':bool(is_like),
    }
    return render(request, 'blog/post_detail.html' , context)

def add_comment(request,id):
    post= get_object_or_404(Post, id=id)
    comment = Comment.objects.create(user=request.user, post=post , content=request.POST['comment'])
    comment.save()
    
    comments=Comment.objects.all()
    like = Like.objects.all().filter(post=id).count()
    is_like = Like.objects.filter(user=request.user, post=post)
    
    context = {
        'post':post,
        'comments': comments,
        'like': like,
        'is_like':bool(is_like),
    }
    return render(request, 'blog/post_detail.html' , context)

def add_like(request,id):
    post= get_object_or_404(Post, id=id)
    comments=Comment.objects.all()
    is_like = Like.objects.filter(user=request.user, post=post)
    if bool(is_like):
        is_like.delete()
    else:
        likeY = Like.objects.create(user=request.user , post=post)
        likeY.save()
        
    like = Like.objects.all().filter(post=id).count()
    is_like = Like.objects.filter(user=request.user, post=post)
    context = {
        'post':post,
        'comments': comments,
        'like': like,
        'is_like':bool(is_like),
    }
    return render(request, 'blog/post_detail.html' , context)
    
  
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            formY = form.save(commit=False)
            formY.user = request.user
            formY.save()
            return redirect('/')
        
    context={
        'form':form,
    }
    return render (request, 'blog/add_post.html', context)

def update_post(request,id):
    post = Post.objects.get(id=id)
    # post = get_object_or_404(Post , id=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST , instance=post)
        if form.is_valid:
            form.save()
            return redirect('/')
        
    context={
        'form' : form,
    }
    return render (request, 'blog/update_post.html', context)
        
    



    
def delete_post(request,id):
    post=get_object_or_404(Post , id=id)
    if request.method == 'POST':
        post.delete()
        return redirect ('/')
     
    context = {
        'post':post
    }
    return render(request, 'blog/delete_post.html',context)
    
def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'registration/register.html',context )