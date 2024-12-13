from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Category, Post


def index(request):
    now = timezone.now()
    template = 'blog/index.html'
    posts = Post.objects.order_by('id').filter(
        is_published=True,
        created_at__lte=now,
        category__is_published=True)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.filter(
            is_published=True,
            category__is_published=True
        ),
        pk=post_id)
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    now = timezone.now()
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        created_at__lte=now
    ).order_by('-created_at')
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, template, context)
