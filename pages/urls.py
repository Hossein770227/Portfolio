from django.urls import path

app_name = 'pages'

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('message/', views.ReciveMessage.as_view(), name='recive_message'),
]
