from django.shortcuts import (
    render, get_object_or_404, redirect
)
from django.utils import timezone

from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   
    return render(request, 'blog/post_list.html', {'posts': posts})
    

def post_detail(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)    
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

        return redirect('post_detail', id=post.id)
    
    # GET    
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)

    # GET    
    form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})