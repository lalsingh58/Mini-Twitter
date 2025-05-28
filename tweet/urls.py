from django.contrib import admin
from django.urls import path
from .views import display_tweet,delete_tweet,create_tweet,edit_tweet,register

urlpatterns = [
    path('',display_tweet,name='display_tweet'),
    path('create/',create_tweet,name='create_tweet'),
    path('<int:tweet_id>/delete/',delete_tweet,name='delete_tweet'),
    path('<int:tweet_id>/edit/',edit_tweet,name='edit_tweet'),
    path('register/',register,name='register'),
]  