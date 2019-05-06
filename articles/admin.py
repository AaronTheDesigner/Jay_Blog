from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Cover, Novel, Event, Novella, Short, Feature

# Register your models here.
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Cover, ArticleAdmin)
admin.site.register(Novel, ArticleAdmin)
admin.site.register(Event, ArticleAdmin)
admin.site.register(Novella, ArticleAdmin)
admin.site.register(Short, ArticleAdmin)
admin.site.register(Feature, ArticleAdmin)

