#-*- coding: utf-8 -*-

from django.db import models
from django.db.models import signals, get_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.conf import settings


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')

    def get_absolute_url(self):
        return reverse('favorites', kwargs={'user_id': str(self.user_id), })

    def __unicode__(self):
        return "%s likes %s" % (self.user, self.content_object)


def setup_generic_relations():
    """
    Set up (reverse) GenericRelations for related models on the fly.
    """
    for app_model in getattr(settings, 'FAVORITE_MODELS', []):
        model = get_model(*app_model.split('.'))
        if model is None:
            raise ValueError('%s model does not exists or is not installed yet' % app_model)
        generic.GenericRelation(Favorite,
            content_type_field='content_type',
            object_id_field='object_id',
        ).contribute_to_class(model, 'favorites')

setup_generic_relations()


def favorite_relation_check(sender, instance, raw, using, **kwargs):
    models = [get_model(*app_model.split('.')) for app_model in getattr(settings, 'FAVORITE_MODELS', [])]
    if instance.content_object.__class__ not in models:
        raise ValueError('%s model not found in FAVORITE_MODELS' % instance.content_object.__class__.__name__)


signals.pre_save.connect(favorite_relation_check, sender=Favorite, dispatch_uid=__name__)