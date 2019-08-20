from django.urls import path
from .views import ArticleListView, ArticleDetailView
from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-home'),
    path('/<int:pk>/', ArticleDetailView.as_view(), name='article-detail')
    
]
