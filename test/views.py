#-*- coding: utf-8 -*-
from django.views.generic import DetailView

from models import Article


class SingleArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = 'article.html'