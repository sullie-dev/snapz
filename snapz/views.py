from django.shortcuts import render, get_object_or_404, reverse,redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from snapzapp.models import Post, Comment
from .forms import CommentForm, PostForm
import random
import string


def idGenerator():
    upper_string = string.ascii_uppercase
    lower_string = string.ascii_lowercase
    numerical = string.digits

    alphabet = upper_string + lower_string + numerical
    random_character = random.sample(alphabet, 10)
    slug = "".join(random_character)
    return slug


randString = idGenerator()


class PostList(generic.ListView):
    def get(self, request,  *args, **kwargs):
        posts = Post.objects.all()
        return render(
            request,
            'index.html',
            {
                'posts': posts
            }
        )


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        postQueryset = Post.objects.filter(slug=slug)
        post = get_object_or_404(postQueryset, slug=slug)
        comments = post.comments.filter(post=post).order_by("-created_on")

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post.html",
            {
                'posts': post,
                'comments': comments,
                'comment_form': CommentForm(),
                'liked': liked
            },
        )

    def post(self, request, slug, *args, **kwargs):
        postQueryset = Post.objects.filter(slug=slug)
        post = get_object_or_404(postQueryset, slug=slug)

        comments = post.comments.filter(post=post).order_by("-created_on")

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse('post', args=[slug]))


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post', args=[slug]))


class PostNewImage(View):
    def get(self, request):
        return render(
                request,
                "new.html",
                {
                    "post_form": PostForm
                }
                )

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = randString
            post_form.instance.post_id = randString
            post = post_form.save(commit=False)
            post.save()
            print(request.FILES)
        else:
            post_form = PostForm()

        return HttpResponseRedirect(reverse('home'))


class AccoountView(View):
    def get(self, request, slug,  *args, **kwargs):
        user = User.objects.get(username=slug)
        posts = Post.objects.all().filter(author=user)

        return render(
            request,
            'account.html',
            {
                'posts': posts,
                'author': user
            }
        )


class Error404Page(View):
    def get(request):
        return render('error.html')