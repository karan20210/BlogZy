from curses.ascii import HT
import email
import re
from turtle import title
import django
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from pymysql import NULL
from home.models import Contact
from django.contrib import messages
from blog.models import Blog, BlogComment
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        query = request.POST['query']
    
        if(len(phone) < 10 or len(name) < 1 or len(email) < 3 or len(query) < 1):
            messages.error(request, "Invalid Entries")
        else:
            contact = Contact(name = name, email = email, phone = phone, desc = query)
            contact.save()
            messages.success(request, "Your query has been recieved!")

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['search']
    blogTitle = Blog.objects.filter(title__icontains = query)
    blogContents = Blog.objects.filter(content__icontains = query)
    blog = blogTitle.union(blogContents)
    context = {'allBlogs': blog, 'query': query}
    return render(request, 'home/search.html', context)

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']

        if(pwd != cpwd):
            messages.error(request, "Passwords do not match")
            return redirect('home')

        newUser = User.objects.create(username = name, email = email, password = pwd, is_staff = True)
        newUser.role = "Blog writers"
        group = Group.objects.get(name='Blog writers')        
        newUser.save()
        newUser.groups.add(group)
        messages.success(request, "Successfully signed up!")
        return redirect('home')
    else:
        return HttpResponse("Cannot signup")

def loginPage(request):
    if request.method == 'POST':        
        username = request.POST['username']
        pwd = request.POST['pwd']

        print(username, pwd)

        user = authenticate(username = username, password = pwd)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!!")
            return redirect('home')
    return HttpResponse("404-Not found")

def logoutPage(request):
    logout(request)       
    messages.success(request, "Successfully logged out!")
    return redirect('home')

def postComment(request, slug):    
    if(request.method == 'POST'):
        url = "/blog/" + slug
        comment = request.POST['comment']
        current_user = request.user
        blog = Blog.objects.filter(slug = slug).first()
        if current_user.is_anonymous:
            messages.error(request, "You need to be signed in to comment")
            return redirect(url)
        newComment = BlogComment(comment = comment, user = current_user, blog = blog)
        newComment.save()
        return redirect(url)

    