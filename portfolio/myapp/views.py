from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def Banner(request):
    return render(request, 'homepage.html')

def Education(request):
    return render(request, 'about.html')

def Portfolio(request):
    return render(request, 'portfolio.html')

def Service(request):
    return render(request, 'service.html')

def Likes(request):
    return render(request, 'likes.html')

def Food_Detail(request):
    return render(request, 'food-detail-page.html')

def Game_Detail(request):
    return render(request, 'games-detail-page.html')

def Football_Detail(request):
    return render(request, 'football-detail-page.html')

def blog_base(request):
    return render(request, 'blog-base.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})



def contact(request):
    return render(request, 'contact.html')