from typing import Any
from django.shortcuts import render
from django.views import generic
from django.utils.translation import gettext as _

from .forms import ReciveMessageForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Skills


def home_page_view(request):
    skills = Skills.objects.filter(active=True)
    return render(request,'pages/home.html',{'skills':skills})


class ReciveMessage(SuccessMessageMixin,generic.CreateView, LoginRequiredMixin):
    form_class = ReciveMessageForm
    template_name = 'pages/home.html'
    success_message =_('your message successfully submit')