from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccess, name='signup_success'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('candidate_profile/', views.candidate_edit_profile, name='candidate_profile'),
    path('examiner_profile/', views.examiner_edit_profile, name='examiner_profile'),
    path('candidate_detail/', views.candidate_profile, name='candidate_detail'),
    path('examiner_detail/', views.examiner_profile, name='examiner_detail'),
    path('update_candidate/', views.update_candidate, name='update_candidate'),
    path('update_examiner/', views.update_examiner, name='update_examiner'),

]