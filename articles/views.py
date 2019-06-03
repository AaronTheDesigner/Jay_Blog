from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Cover, Novel, Event, Novella, Short, Feature

def main(request):
    covers = Cover.objects.all()
    novels = Novel.objects.all()
    events = Event.objects.all()
    novellas = Novella.objects.all()
    shorts = Short.objects.all()
    features = Feature.objects.all()

    return render(request, 'main.html', {
        'covers': covers,
        'novels': novels,
        'events': events,
        'novellas': novellas,
        'shorts': shorts,
        'features': features
    })



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




