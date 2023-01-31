from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTutorial),
    #path('<int:pk>/', views.tutorial_detail), 
    #path('', views.ListTodo.as_view()),
    #path('<int:pk>/', views.DetailTodo.as_view()),
]