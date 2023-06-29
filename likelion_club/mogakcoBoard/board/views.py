from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm 
from django.utils import timezone

# Create your views here.

def home(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail': post_detail, 'comment_form': comment_form})

def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('detail', post_id)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    # 댓글을 썼던 post detail 페이지로 이동
    return redirect('detail', comment.post.id)

def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        # 폼을 불러올 때 입력했던 내용을 포함시켜 불러오기: instance=post
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now() # 수정일시 저장
            post.save()
            return redirect('detail', post.id )
        
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})
