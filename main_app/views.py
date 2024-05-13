from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

@login_required
def landing_page(request):
    posts = Post.objects.filter(user=request.user).order_by('-posting_date_time')
    return render(request, 'main_app/landing_page.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()  # Save the many-to-many data for the form.
            return redirect('landing_page')
    else:
        form = PostForm()
    return render(request, 'main_app/create_post.html', {'form': form})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main_app/post_detail.html', {'post': post})

@login_required
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

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('landing_page')
    return render(request, 'main_app/delete_post.html', {'post': post})

@login_required
def volunteer_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    volunteer_id = request.user.id
    user = User.objects.get(id=volunteer_id)
    if user not in post.volunteer_ids.all():
        post.volunteer_ids.add(user)
        post.save()
    return redirect('post_detail', post_id=post.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    volunteered_posts = user.volunteered_posts.all()
    return render(request, 'main_app/profile.html', {
        'user': user,
        'posts': posts,
        'volunteered_posts': volunteered_posts,
    })