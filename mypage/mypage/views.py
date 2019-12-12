from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from mypage.models import Blog

from mypage.form import Blogform, LoginForm


def blog_list(request):

    user = request.user

    if user.is_anonymous:
        blogs = Blog.objects.filter(privacy=Blog.PUBLIC)
    else:
        blogs = Blog.objects.all()

    blogs = blogs.order_by('-date')
    print(blogs)
    context = dict(blogs=blogs)

    return render(request=request, template_name='blog_list.html', context=context)


def blog_create(request):

    user = request.user
    form = Blogform(user=user)

    if request.method == "POST":

        form = Blogform(user=user, data=request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, 'Created a new blog')
            return redirect(reverse('index'))
        print(form.errors)

    context = dict(form=form)
    return render(request=request, template_name='blog_create.html', context=context)


def blog_view(request, id):

    blog = Blog.objects.filter(id=id).first()

    context = dict(blog=blog)

    return render(request, 'blog_view.html', context=context)


def edit_view(request,id):
    blog = Blog.objects.filter(id=id).first()
    context = dict(blog=blog)
    return render(request, 'edit_view.html', context=context)



def login_view(request):

    form = LoginForm(request=request)

    if request.method == "POST":
        form = LoginForm(data=request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.filter(email=email).first()

            #user = auth.authenticate(username=user.username, password=password)
            print(user, email, password)
            #1/0
            # User is valid.
            if user:
                login(request=request, user=user)
                messages.success(request, "Logged in")
                return redirect(reverse('blog_create'))
        else:
            messages.error(request, form.errors)
            return redirect("/")

    context = dict(form=form)
    return render(request, 'login.html', context=context)


def logout_view(request):

    if request.user.is_authenticated:

        logout(request)
        messages.success(request,"Logged out")

    return redirect("/")