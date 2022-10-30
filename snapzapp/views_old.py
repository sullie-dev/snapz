from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import generic, View

from snapz.forms import CommentForm
from snapzapp.models import Post, Comment


# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "index.html"

# def home(request):
    # posts = Post.objects.all()
    # context = {
    #     'posts': posts,
    # }
    # for post in posts:
    #     print(post.likes)
    # return render(request, 'index.html',  context)


# def viewPost(request, slug, *args, **kwargs):
#     postQueryset = Post.objects.filter(slug=slug)
#     post = get_object_or_404(postQueryset, slug=slug)
#     comments = post.comments.filter(post=post).order_by("-created_on")


#     context = {
#         'posts': post,
#         'comments': comments,
#         'comment_form': CommentForm()
#     }
#     return render(request, 'post.html', context)


def likePost(request, slug, *args, **kwargs):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    posts = Post.objects.all()
    liked = False
    if post.likes.filter(id=self.request.user.id).exists():
        liked = True
    context = {
        'posts': posts,
        'liked': liked
    }
    return render(request, 'index.html',  context)


def comment(request, slug,  *args, **kwargs):
    post_id = slug
    postQueryset = Post.objects.filter(slug=slug)
    post = get_object_or_404(postQueryset, slug=slug)

    liked = False
    if post.likes.filter(id=self.request.user.id).exists():
        liked = True

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
        'comment_form': CommentForm(),
        'liked': liked
    }

    return render(request, 'post.html', context)


def account(request, slug,  *args, **kwargs):
    user = User.objects.get(username=slug)
    posts = Post.objects.all().filter(author=user)

    context = {
        'posts': posts,
    }

    return render(request, 'account.html',  context)
