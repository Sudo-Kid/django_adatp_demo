import logging

from django.shortcuts import render
from django.views.generic import View

from . import adapt
from . import forms


logger = logging.getLogger(__name__)


class Index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        form = forms.AdaptForm()
        return render(request, self.template_name,
                      {'form': form, 'locations': adapt.locations})

    def post(self, request, *args, **kwargs):
        form = forms.AdaptForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            form.save()
            response = adapt.get_intent(question.message)
            form = forms.AdaptForm()
            return render(request, self.template_name,
                          {'form': form, 'locations': adapt.locations, 'response': response})
        else:
            logger.warning('Something went wrong')

        return render(request, self.template_name,
                      {'form': form, 'locations': adapt.locations})
