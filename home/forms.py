from django import forms

from . import models


class AdaptForm(forms.ModelForm):
    class Meta:
        model = models.AdaptMessage
        fields = ('message', )
