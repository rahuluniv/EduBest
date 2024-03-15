from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pkid>/', views.UserDetailView.as_view(), name='user-detail'),
]
