from django.urls import path

from students import views

app_name = 'student'
urlpatterns = [
    path('select_subject/', views.select_subject, name='select_subject'),
    path('get_question/', views.get_question, name='get_question'),
    path('question/', views.question, name='question')
]
