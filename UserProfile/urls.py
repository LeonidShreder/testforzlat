from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from UserProfile import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/friends/<int:pk>/', views.UserFriends.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)