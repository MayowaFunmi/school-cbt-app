from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('question/', views.civic_ss3, name='question'),
    path('que/', views.CreateQue.as_view(), name='que')
]