from django.urls import path

from book import views

urlpatterns = [
    path('index/<int:pk>/', views.index, name='index'),
    path('', views.base, name='base'),
    path('lesson_detail/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('search/', views.Search.as_view(), name='search')
]