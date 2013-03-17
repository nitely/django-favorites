#-*- coding: utf-8 -*-

from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import Favorite
from ..forms import FavoriteForm

register = template.Library()


@register.inclusion_tag('favorites/form.html')
def render_favorite_form(model_instance, user, next=None):
    content_type = ContentType.objects.get_for_model(model_instance)

    try:
        favorite = Favorite.objects.get(user=user,
            content_type=content_type,
            object_id=model_instance.pk)
    except Favorite.DoesNotExist:
        favorite = None

    form = FavoriteForm(initial={'content_type': content_type, 'object_id': model_instance.pk})

    return {'form': form, 'favorite': favorite, 'next': next}


@register.simple_tag()
def get_favorites_count(user):
    return Favorite.objects.filter(user=user).count()