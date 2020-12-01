from django.urls import path

from exam_question import views, list_views

app_name = 'exam_question'

urlpatterns = [
    path('exam_register/', list_views.examiner_exam_reg, name='exam_register'),
    path('choose_exam/', views.choose_exam, name='choose_exam'),
    path('check_question/', views.check_question, name='check_question'),
    path('my_details/', list_views.examiner_details, name='my_details'),
    path('my_questions/', list_views.list_questions, name='my_questions'),
    path('edit/<str:question_id>/', views.edit_question, name='edit'),


    # financial accounting questions
    path('account_ss1/', views.accounts_ss1, name='account_1'),
    path('account_ss2/', views.accounts_ss2, name='account_2'),
    path('account_ss3/', views.accounts_ss3, name='account_3'),

    # agric questions
    path('agric_ss1/', views.agric_ss1, name='agric_1'),
    path('agric_ss2/', views.agric_ss2, name='agric_2'),
    path('agric_ss3/', views.agric_ss3, name='agric_3'),

    # biology questions
    path('biology_ss1/', views.biology_ss1, name='biology_1'),
    path('biology_ss2/', views.biology_ss2, name='biology_2'),
    path('biology_ss3/', views.biology_ss3, name='biology_3'),

    # chemistry questions
    path('chemistry_ss1/', views.chemistry_ss1, name='chemistry_1'),
    path('chemistry_ss2/', views.chemistry_ss2, name='chemistry_2'),
    path('chemistry_ss3/', views.chemistry_ss3, name='chemistry_3'),

    # civic questions
    path('civic_ss1/', views.civic_ss1, name='civic_1'),
    path('civic_ss2/', views.civic_ss2, name='civic_2'),
    path('civic_ss3/', views.civic_ss3, name='civic_3'),

    # commerce questions
    path('commerce_ss1/', views.commerce_ss1, name='commerce_1'),
    path('commerce_ss2/', views.commerce_ss2, name='commerce_2'),
    path('commerce_ss3/', views.commerce_ss3, name='commerce_3'),

    # crs questions
    path('crs_ss1/', views.crs_ss1, name='crs_1'),
    path('crs_ss2/', views.crs_ss2, name='crs_2'),
    path('crs_ss3/', views.crs_ss3, name='crs_3'),

    # economics questions
    path('economics_ss1/', views.economics_ss1, name='economics_1'),
    path('economics_ss2/', views.economics_ss2, name='economics_2'),
    path('economics_ss3/', views.economics_ss3, name='economics_3'),

    # english literature questions
    path('eng_literature_ss1/', views.eng_literature_ss1, name='eng_lit_1'),
    path('eng_literature_ss2/', views.eng_literature_ss2, name='eng_lit_2'),
    path('eng_literature_ss3/', views.eng_literature_ss3, name='eng_lit_3'),

    # english questions
    path('english_ss1/', views.english_ss1, name='english_1'),
    path('english_ss2/', views.english_ss2, name='english_2'),
    path('english_ss3/', views.english_ss3, name='english_3'),

    # further mathematics questions
    path('further_maths_ss1/', views.further_maths_ss1, name='further_maths_1'),
    path('further_maths_ss2/', views.further_maths_ss2, name='further_maths_2'),
    path('further_maths_ss3/', views.further_maths_ss3, name='further_maths_3'),

    # geography questions
    path('geography_ss1/', views.geography_ss1, name='geography_1'),
    path('geography_ss2/', views.geography_ss2, name='geography_2'),
    path('geography_ss3/', views.geography_ss3, name='geography_3'),

    # government questions
    path('government_ss1/', views.government_ss1, name='government_1'),
    path('government_ss2/', views.government_ss2, name='government_2'),
    path('government_ss3/', views.government_ss3, name='government_3'),

    # marketing questions
    path('marketing_ss1/', views.marketing_ss1, name='marketing_1'),
    path('marketing_ss2/', views.marketing_ss2, name='marketing_2'),
    path('marketing_ss3/', views.marketing_ss3, name='marketing_3'),

    # mathematics questions
    path('maths_ss1/', views.maths_ss1, name='maths_1'),
    path('maths_ss2/', views.maths_ss2, name='maths_2'),
    path('maths_ss3/', views.maths_ss3, name='maths_3'),

    # physics questions
    path('physics_ss1/', views.physics_ss1, name='physics_1'),
    path('physics_ss2/', views.physics_ss2, name='physics_2'),
    path('physics_ss3/', views.physics_ss3, name='physics_3'),

    # yoruba questions
    path('yoruba_ss1/', views.yoruba_ss1, name='yoruba_1'),
    path('yoruba_ss2/', views.yoruba_ss2, name='yoruba_2'),
    path('yoruba_ss3/', views.yoruba_ss3, name='yoruba_3'),

]