from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog, BlogComment

# Create your views here.
def bloghome(request):
    allBlogs = Blog.objects.all()
    context = {"allBlogs": allBlogs}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    blog = Blog.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(blog = blog)
    for i in comments:
        print(i)
    context = {"blog": blog, "slug": slug, "comments": comments}
    return render(request, 'blog/blogPost.html', context)
