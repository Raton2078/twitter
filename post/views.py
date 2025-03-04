from django.shortcuts import render, redirect
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required



def create_post(request):
    if request.method == 'POST':
      form = forms.CreatePost(request.POST)
      if form.is_valid():
         newpost = form.save(commit=False)
         newpost.auteur = request.user
         newpost.save()
         return redirect('/')
    else:
       form = forms.CreatePost()
       return render(request, "post/create_post.html", {"form": form})  


def see_all_post(request):
   posts = Post.objects.all()
   return render(request, 'post/all_posts.html', {'posts': posts})




   



@login_required 
def see_self_post(request):

    posts = Post.objects.filter(auteur=request.user)
    print(posts)
    return render(request, 'post/self_posts.html',{'posts': posts})

# Create your views here.
