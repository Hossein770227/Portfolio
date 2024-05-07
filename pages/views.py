from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import ReciveMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name ='pages/home.html'


class ReciveMessage(generic.CreateView, LoginRequiredMixin):
    form_class = ReciveMessageForm
    template_name = 'pages/home.html'
