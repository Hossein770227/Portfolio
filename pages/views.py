from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import ReciveMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Skills

# class HomePageView(TemplateView):
#     template_name ='pages/home.html'

def home_page_view(request):
    skills = Skills.objects.filter(active=True)
    return render(request,'pages/home.html',{'skills':skills})


class ReciveMessage(generic.CreateView, LoginRequiredMixin):
    form_class = ReciveMessageForm
    template_name = 'pages/home.html'
