from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from .forms import *
from .models import Like

@login_required(login_url='login/')
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method == 'GET':

        Posts = Photos.objects.all()
        Comments = Comment.objects.all()
        return render(request, 'main/index.html', {'post': Posts,
                                                   'comment': Comments})

    post = Photos.objects.all()
    user = request.user
    comment = Comment.objects.all()

    context = {
        'post': post,
        'user': user,
        'comment': comment,
    }

    return render(request, "main/index.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "main/login.html", {"message": "Invalid user"})
        return render(request, 'main/login.html')

@login_required(login_url='login/')
def logout_view(request):
    logout(request)
    return render(request, 'main/logout.html')

def registration_view(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        context = {'form': form}

        return render(request, 'main/registration.html', context)

@login_required(login_url='login/')
def edit_view(request):

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('menu')

    else:
        form = EditProfile(instance=request.user)
        context = {'form': form}

        return render(request, 'main/editprofile.html', context)

def picture_edit(request):

    user = request.user.profile
    form = ProfileImage(instance=user)

    if request.method == 'POST':
        form = ProfileImage(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit')

    context = {'form': form}

    return render(request, 'main/editpic.html', context)

def photo_feed(request):
    user = request.user
    form = PhotoFeed(instance=user)

    if request.method == 'POST':

        form = PhotoFeed(request.POST, request.FILES or None, instance=user)

        if form.is_valid():
            post = Photos(user=user, post=request.FILES['post'])
            post.save()
            return redirect('home')

    posts = Photos.objects.filter(user=user)

    context = {'form': form,
               'posts': posts}

    return render(request, 'main/menu.html', context)

def like_post(request):
    user = request.user

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Photos.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value == 'Unlike'
            else:
                like.value = 'Like'

        like.save()

    return redirect('home')

def search_user(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        user = User.objects.all().filter(username__icontains=search)
        return render(request, 'main/search_user.html', {'user': user})

def comment(request):
    user = request.user
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=user)
        if comment_form.is_valid():
            comment_form.save()
            print(request.POST)
            return redirect('home')
    else:
        comment_form = CommentForm()

    context = {'comment_form': comment_form}

    return render(request, 'main/commentform.html', context)


def open_user_view(request, uid):
    user = User.objects.get(id=uid)
    posts = Photos.objects.filter(user=user)

    return render(request, 'main/userview.html', {'user': user, 'posts': posts})