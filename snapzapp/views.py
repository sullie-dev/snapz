from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from snapz.forms import CommentForm
from snapzapp.models import Post, Comment


# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    context = {
        'posts': posts,
    }
    return render(request, 'index.html',  context)


def viewPost(request, slug, *args, **kwargs):
    postQueryset = Post.objects.filter(slug=slug)
    post = get_object_or_404(postQueryset, slug=slug)
    comments = post.comments.filter(post=post).order_by("-created_on")

    context = {
        'posts': post,
        'comments': comments,
        'comment_form': CommentForm()
    }
    return render(request, 'post.html', context)


def comment(request, slug,  *args, **kwargs):
    post_id = slug
    postQueryset = Post.objects.filter(slug=slug)
    post = get_object_or_404(postQueryset, slug=slug)
    comments = post.comments.filter(post=post).order_by("-created_on")

    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'posts': post,
        'comments': comments,
        'comment_form': CommentForm()
    }

    return render(request, 'post.html', context)


def account(request, slug,  *args, **kwargs):
    user = User.objects.get(username=slug)
    posts = Post.objects.all().filter(author=user)

    # comments = post.comments.filter(autor=user).order_by("-created_on")
    context = {
        'posts': posts
        # 'comments': comments,
    }
    return render(request, 'account.html', context)
