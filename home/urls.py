from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^answer$', views.Answer.as_view(), name='Answer'),
]
