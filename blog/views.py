from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
    )
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted'] # orderes posts from newest to oldest
    paginate_by = 5 # makes it 5 posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 # makes it 5 posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

# LoginRequiredMixin redirects user to login page if they try to create new post withour being logged in
class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content'] # Fields in the create post section

    # Makes currently logged in user the valid user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content'] # Fields in the create post section

    # Makes currently logged in user the valid user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: # checks if current user is the author
            return True
        return False # if user is not author they will not be able to edit post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: # checks if current user is the author
            return True
        return False # if user is not author they will not be able to delete post

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
