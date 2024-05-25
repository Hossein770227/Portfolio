
import os
from django.shortcuts import render
from django.views import generic
from django.utils.translation import gettext as _


from django.conf import settings
from django.http import FileResponse




from .forms import ReciveMessageForm
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from .models import Skills, Portfolio


def home_page_view(request):
    skills = Skills.objects.filter(active=True)
    portfolio = Portfolio.objects.filter(active=True)
    return render(request,'pages/home.html',{'skills':skills,'portfolios':portfolio})


class ReciveMessage(SuccessMessageMixin,generic.CreateView):
    form_class = ReciveMessageForm
    http_method_names =['post']
    template_name = 'pages/home.html'
    success_message =_('your message successfully submit')



def download(request):
    file = os.path.join(settings.BASE_DIR, 'file/rezomeh.pdf')
    file_open = open(file, 'rb')
    return FileResponse(file_open)