from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import PostForm, CommentForm, CategoryForm
from .models import Comment, Post, Category


def posts_list(request):
    category_filter = request.GET.get('c')
    query_set = Post.objects.all()
    if category_filter:
        query_set = query_set.filter(categories__in=category_filter)
    posts = query_set.annotate(comments_count=Count('comments'))
    return render(request, 'forum/posts_list.html', {'posts': posts})


def post_read(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = post.comments.order_by('-published_at')
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})


@login_required
def post_create(request):
    category_form = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_read', post_pk=post.pk)
    else:
        form = PostForm()
        category_form = CategoryForm()
    return render(request, 'forum/post_edit.html', {'form': form, 'modal_form': category_form})


@login_required
def post_update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    category_form = None
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_read', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
        category_form = CategoryForm()
    return render(request, 'forum/post_edit.html', {'form': form, 'modal_form': category_form})


@login_required
def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    post_url = reverse('posts_list')
    return redirect(post_url)


@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'post': post})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            post.updated_at = timezone.now()
            post.save()

            return redirect(reverse('post_read', kwargs={'post_pk': post_pk}))
    else:
        form = CommentForm()
    return render(request, 'forum/comment_edit.html', {'post': post, 'form': form})


@login_required
def comment_update(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'post': comment.post}, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)

            post = comment.post
            post.updated_at = timezone.now()
            post.save()

            comment.save()

            return redirect(reverse('post_read', kwargs={'post_pk': post_pk}))
    else:
        form = CommentForm(instance=comment)
    post = Post.objects.get(pk=post_pk)
    return render(request, 'forum/comment_edit.html', {'post': post, 'form': form})


@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    post_url = reverse('post_read', kwargs={'post_pk': post_pk})
    return redirect(post_url)


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()
    return render(request, 'forum/category_edit.html', {'form': form})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/categories_list.html', {'categories': categories})


@login_required
def category_update(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'forum/category_edit.html', {'form': form})


@login_required
def category_delete(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    category.delete()
    post_url = reverse('categories_list')
    return redirect(post_url)
