from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from neighbourhoodwatch.models import Post, Profile, Business, Neighbourhood
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "main/signup.html", context={'form': form})

class PostListView(ListView):
    model = Post
    template_name = "main/index.html"
    context_object_name = "posts"
    ordering =['-post_date']

class PostCreateView(CreateView):
    model = Post
    template_name = "main/postform.html"
    fields = ['title', 'message']