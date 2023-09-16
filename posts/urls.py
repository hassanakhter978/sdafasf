from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('api/posts/', views.listAll_and_create_view, name='listAll_and_create_view'),
    path('api/posts/<int:pk>/', views.post_detail_view, name='post-detail'),

]