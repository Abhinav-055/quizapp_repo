from django.urls import path
from .views import quiz_detail, submit_quiz,create_quiz
from . import views
app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', create_quiz, name='create_quiz'),
    path('<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('<int:quiz_id>/submit/', submit_quiz, name='submit_quiz'),
    path('quiz_list/', views.quiz_list, name='quiz_list'),
]