#-*- coding: utf-8 -*-

from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model

from models import Favorite
from forms import FavoriteForm


@login_required
@require_POST
def favorite_create(request):
    form = FavoriteForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
    return redirect(request.POST.get('next', '/'))


@login_required
@require_POST
def favorite_delete(request, pk):
    favorite = get_object_or_404(Favorite, pk=pk, user=request.user)
    favorite.delete()
    return redirect(request.POST.get('next', '/'))


class FavoritesDetail(DetailView):
    context_object_name = "favorites"
    model = Favorite
    template_name = 'favorites/list.html'

    def get_object(self, queryset=None):
        return Favorite.objects.filter(user__username=self.kwargs['username']).prefetch_related('content_object')

    def get_context_data(self, **kwargs):
        context = super(FavoritesDetail, self).get_context_data(**kwargs)
        context['fav_user'] = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FavoritesDetail, self).dispatch(*args, **kwargs)