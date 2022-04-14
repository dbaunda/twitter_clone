from ast import If
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def index(request):
    form = PostForm(request.POST, request.FILES) 
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        # If the form is valid
        if form.is_valid():

            # Yes, Save
            form.save() 

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            #No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

#get all posts, limit 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    #show
    return render(request, 'posts.html', {'posts': posts, 'form': form})

def delete(request, post_id):
    #find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')



def likes(request, id):
    liked = Post.objects.get(id=id)
    liked.like_count += 1
    liked.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})