from django.shortcuts import render, get_object_or_404
from .models import Blog_project

def all_blogs(request):
    blog_projects = Blog_project.objects.order_by('-date_blog')
    return render(request, 'blog/all_blogs.html', {'blog_projects': blog_projects})


def detail(request, blog_id):
    blog = get_object_or_404(Blog_project, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})