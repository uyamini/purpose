from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, User
from .forms import PostForm

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
    # assume volunteer ID is 1 (since there's no user auth)
    volunteer_id = 1
    user = User.objects.get(id=volunteer_id)
    if user not in post.volunteer_ids.all():
        post.volunteer_ids.add(user)
        post.save()
    return redirect('post_detail', post_id=post.id)
