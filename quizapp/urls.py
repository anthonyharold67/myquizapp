from django.urls import path
from .views import CategoryView, QuestionView, QuizView

urlpatterns = [
    path("",CategoryView.as_view()),
    path("quiz/<str:category>/",QuizView.as_view()),
    path("quiz/<str:category>/<str:title>/",QuestionView.as_view()),
    
]

