from django.shortcuts import render
from articles.models import Cover, Novel, Event, Novella, Short, Feature

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