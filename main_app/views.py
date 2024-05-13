from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def landing_page(request):
    posts = Post.objects.all().order_by('-posting_date_time')
    return render(request, 'main_app/landing_page.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = PostForm()
    return render(request, 'main_app/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main_app/post_detail.html', {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'main_app/edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('landing_page')
    return render(request, 'main_app/delete_post.html', {'post': post})

def volunteer_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Simulate volunteering by adding a dummy user ID (since there's no user auth)
    # You can replace this logic as needed
    volunteer_id = 1  # Simulated volunteer ID
    if volunteer_id not in post.volunteer_ids.all():
        post.volunteer_ids.add(volunteer_id)
        post.save()
    return redirect('post_detail', post_id=post.id)

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('landing_page')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('landing_page')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})