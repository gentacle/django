from django.shortcuts import redirect, render, get_object_or_404
from django.db import models
from django.utils import timezone

from .forms import PostForm
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html',{
        'posts' : posts,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })


def post_new(request):
    if request.method == 'POST':
        #폼을 입력 후 '저장' 을 눌렀을 때
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #처음 빈 폼을 보여줄 때
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        #폼을 입력 후 '저장' 을 눌렀을 때
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #처음 빈 폼을 보여줄 때
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})
