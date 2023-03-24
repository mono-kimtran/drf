from django.urls import path
from .views import profile_view, profile_update_view

app_name = 'users'
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile-update/', profile_update_view, name='profile-update'),
]
