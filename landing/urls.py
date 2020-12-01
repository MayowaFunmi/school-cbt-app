from django.urls import path
from . import views
app_name = 'landing'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('instruction/', views.instruction, name='instruction'),
    path('members/', views.members, name='members'),
    path('details/', views.exam_details, name='details'),

]