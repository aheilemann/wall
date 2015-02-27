from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PostForm, CommentForm
from .models import Post, Comment


def example_html_view(request):
    return render(request, 'example_view.html', {})


def post_list(request):
    posts = Post.objects.all()
    post = Post.objects.get(pk=1)
    comments = post.comment_set.all()

    return render(
        request, 
        'wall/post_list.html', {
            'wall_posts': posts, 'wall_comments': comments,
        }
    )


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()

    return render(
        request,
        'wall/post_details.html', {
            'post': post, 
        }
    )


def post_write_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_wall')
    else:
        form = PostForm()

    return render(
        request, 
        'wall/post_new.html', {
            'form': form,
        }
    )


def comment_write_new(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
            return redirect('post_wall')
    else:
        form = CommentForm()


    return render(
        request, 
        'wall/comment_new.html', {
            'post': post, 'comment': form,
        }
    )


