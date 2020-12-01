from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings

app_name = 'exams'

urlpatterns = [
    path('add_department/', views.add_department, name='add_department'),
    path('add_department_save/', views.add_department_save, name='add_department_save'),
    path('edit_department/', views.edit_department, name='edit_department'),
    path('edit_department_save/', views.edit_department_save, name='edit_department_save'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_subject_save/', views.add_subject_save, name='add_subject_save'),
    path('add_student_class/', views.add_student_class, name='add_student_class'),
    path('add_student_class_save/', views.add_student_class_save, name='add_student_class_save'),
    path('add_student_level/', views.add_student_level, name='add_student_level'),
    path('add_student_level_save/', views.add_student_level_save, name='add_student_level_save'),

    path('ajax_question/', views.set_ajax_question, name='ajax_question'),
    path('create_question/', views.CreateQuestion.as_view(), name='create_question'),
    path('update_question/', views.UpdateQuestion.as_view(), name='update_question'),

    path('radio_question/', views.answer, name='radio_question'),

    path('register/', views.register_exam, name='register_exam'),
    path('question/', views.exam_question, name='question'),
    path('answer/', views.student_answer, name='answer'),

]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''