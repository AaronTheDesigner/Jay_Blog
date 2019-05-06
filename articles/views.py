from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.



def home(request):
    context = {
        'articles' : Article.objects.all().order_by('-date_posted')
    }
    return render (request, 'articles/home.html', context)

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/home.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 9

class ArticleDetailView(DetailView):
    model = Article




