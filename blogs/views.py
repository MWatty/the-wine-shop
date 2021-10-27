from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog, Comment
from .forms import BlogForm, CommentForm


# Create your views here.


def all_blogs(request):
    """
    A view to show all blogs along with search queries
    """
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    context = {
        'blogs': blogs,
        'comments': comments,
        'on_blog_page': True,
    }

    return render(request, 'blogs/blogs.html', context)
