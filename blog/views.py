from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

def edit_post(request, id=None):
    item = get_object_or_404(Blog, id=id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
    return render(request, 'post/post_form.html', {'form': form})