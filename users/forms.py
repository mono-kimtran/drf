from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from allauth.socialaccount.forms import SignupForm
from .models import Profile
User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'gender', 'phone', 'address',
                  'profile_pic', 'business_area', 'about',)
