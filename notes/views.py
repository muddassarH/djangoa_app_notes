from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView , UpdateView ,DeleteView
from .models import Notes
from .forms import PostForm
from django.db.models import Q
from django.views import View
from  .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class UserRegisterView(generic.CreateView):
    form_class= RegisterForm
    template_name = 'registration/register.html'
    success_url  = reverse_lazy('login')


class HomeView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'home.html'
    context_object_name = 'items'
    ordering = ['-id']
    # ordering = ['-Note_date']



class ArticleView(DetailView):
    model = Notes
    form_class = PostForm
    template_name = 'articles_details.html'

class AddPostView(LoginRequiredMixin, CreateView):
    model= Notes
    form_class = PostForm
    template_name = 'add_post.html'
    # fields= '__all__'
    # fields = ('title', 'keywords','body')

    
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model= Notes
    form_class = PostForm
    template_name = 'update_post.html'
    # fields= '__all__'



    
class SearchView( LoginRequiredMixin, View):
    template_name = 'search_results.html'

    def get(self, request):
        query = request.GET.get('q')

        if query:
            # Fetch the entire row when a keyword matches
            results = Notes.objects.filter(keywords__icontains=query)
            print(">>>>",results)
        else:
            results = []

        return render(request, self.template_name, {'results': results, 'query': query})
    




class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'delete_note.html'
    success_url = reverse_lazy('home')

