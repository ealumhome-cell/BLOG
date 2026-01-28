from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Post, Status
from django.contrib.auth.models import User

# Create your views here.

class HomePageView(TemplateView):
    template_name="pages/home.html"


class AboutPageView(TemplateView):
    template_name="pages/about.html"

    
class PostListView(ListView):
    """
    PostListView help us to display all posts from the db with a Draft status
    """
    template_name = "posts/List.html"
    #model = Post
    context_object_name = "post"
    #published_status = Status.objects.get(name="Published")
    #Queryset atribute allow us to select some data from the db by using the model class
    #queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()


class PostDraftListView(ListView):
    """
    PostDraftListView help us to display all posts from the db with a Draft status
    """
    template_name = "posts/drafts.html"
    #model = Post
    context_object_name = "drafts"
    #published_status = Status.objects.get(name="drafts")
    #draft_status = Status.object.get(name="drafts")
    #queryset = Post.object.filter(status=draft_status).order_by("created_on").reverse()


class PostArchivedListView(ListView):
    """
    PostArchivedListView help us to display all posts from the db with an Archived status
    """
    template_name = "posts/archived.html"
    #model = Post
    context_object_name = "archived"
    #published_status = Status.objects.get(name="Published")
    #Queryset atribute allow us to select some data from the db by using the model class
    #queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()

class PostDetailView(DetailView):
    """
    PostDetailListView help us to display all posts from the db through the ID.
    """
    template_name = "posts/"
    model = Post


class PostCreateView(CreateView):
   
   template_name = "posts/new.html" 
   model = Post
   fields = ["title", "subtitle", "body"]

def form_valid(self, form):
      print(User.objects.all())
      form.instance.autor = User.object.last()
      return super().form_valid(form)


class PostDeleteView(DeleteView):
    template_name = "posts/delete.html" 
    model = Post
    success_url = reverse_lazy("post_list")
  

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html" 
    model = Post
    fields = ["title", "subtitle", "body"]
        


class LoginPageViews(TemplateView):
    template_name="registration/login.html"