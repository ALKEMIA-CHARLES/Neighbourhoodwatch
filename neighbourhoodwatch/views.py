from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from neighbourhoodwatch.models import Post, Profile, Business, Neighbourhood
from neighbourhoodwatch.forms import UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "main/index.html"
    context_object_name = "posts"
    ordering =['-post_date']

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "main/postform.html"
    fields = ['title', 'message', 'image']
    
    def form_valid(self, form):
        form.instance.masterpost = self.request.user
        return super().form_valid(form)

class NeighbourhoodlistView(LoginRequiredMixin, ListView):
    model = Neighbourhood
    template_name = "main/neighbourhoodlist.html"
    context_object_name = "neighbourhoods"
    ordering = ['-post_date']

class NeighbourDetailView(LoginRequiredMixin, DetailView):
    model = Neighbourhood
    template_name = "main/neighbourhood_detail.html"

class NeighbourCreateView(LoginRequiredMixin, CreateView):
    model = Neighbourhood
    template_name = "main/create_neighbourhood.html"
    fields = ['name', 'image', 'population', 'recommended_by']

    def form_valid(self, form):
        form.instance.recommended_by = self.request.user
        return super().form_valid(form)

class NeighbourUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Neighbourhood
    template_name = "main/create_neighbourhood.html"
    fields = ['name', 'image', 'population', 'recommended_by']

    def form_valid(self, form):
        form.instance.recommended_by = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.recommended_by:
            return True
        return False

class NeighbourDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Neighbourhood
    template_name = 'main/post_confirm_delete.html'
    success_url = 'neighbourhoodlist'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.recommended_by:
            return True
        return False

def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.profile)
    return render(request, "main/profile.html", context={"form":form})

def contactinfo(request):
    return render(request, "main/contactinfo.html")

def businesses(request,id):
    businesses = Business.objects.filter(neighbourhood=get_object_or_404(Neighbourhood,pk=id))
    return render(request, "main/business.html", context={"businesses":businesses})


def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_post = Business.search_businesses_by_name(search_term)
        results = len(searched_post)
        message = "{}".format(search_term)
        
        return render(request, "main/search.html", context={"message":message,
                                                            "posts":searched_post,
                                                            "results":results})
    else:
        message = "You have not searched for any user"
        return render(request, "main/index.html", context={"message":message})
