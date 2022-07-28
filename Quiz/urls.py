from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path("<int:myid>/",quiz, name="quiz"),
    path('<int:myid>/data/', quiz_data_view, name='quiz-data'),
    path('<int:myid>/save/', save_quiz_view, name='quiz-save'),

    path('login/', login_user, name='login'),
    path('signup/',Signup, name='signup'),
    path('teacherSignup/',teacherSignup, name='teacherSignup'),
    path('logout/',logout_user, name='logout'),
 
    path('results-all/', all_results, name='all_results'),
    path('results-maths/', results_math, name='results_maths'),

    path('results/', results, name='results'),
    path('results-history/', results_history, name='results_history'),
    path('results-english/', results_english, name='results_english'),

    path('add_quiz/', add_quiz, name='add_quiz'),    
    path('add_question/', add_question, name='add_question'),  
    path('add_options/<int:myid>/', add_options, name='add_options'), 
    path('results/', results, name='results'),    
    path('delete_question/<int:myid>/',delete_question, name='delete_question'),  
    path('delete_result/<int:myid>/', delete_result, name='delete_result'),
    path('dashboard/', ava, name='dashboard'),
    
    
]
