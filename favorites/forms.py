#-*- coding: utf-8 -*-

from django import forms
from django.contrib.contenttypes.models import ContentType

from models import Favorite


class FavoriteForm(forms.ModelForm):
    # filter(model__in=['model1', 'model2']) is more secure, but allowed models are checked for generic relation later anyway.
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.all(),
        widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Favorite
        exclude = ['date', 'user']

    def clean(self):
        cleaned_data = super(FavoriteForm, self).clean()

        favorite = Favorite.objects.filter(user=self.instance.user,
            content_type=cleaned_data['content_type'],
            object_id=cleaned_data['object_id'])

        if favorite.exists():
            # Do this since some of the unique_together fields are excluded.
            raise forms.ValidationError("This favorite already exists")

        return cleaned_data