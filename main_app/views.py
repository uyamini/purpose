from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
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
