from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by('-create_at')
    return render(request, 'index.html', {'blogs': blogs})


def blog_form(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form = form.save()
            return redirect('read', form.id)
    else:
        form = BlogForm(instance=blog)
        context = {
            'blog_form': form,
            'blog': blog
        }
        return render(request, 'blog/create.html', context)


def create(request):
    return blog_form(request)


def read(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/read.html', {'blog': blog})


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return blog_form(request, blog)


def delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('index')
