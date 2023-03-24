from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
# from django.views.generic import TemplateView, DetailView
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
User = get_user_model()


# @anonymous_require


class SiteLoginView(SuccessMessageMixin, LoginView):
    redirect_authenticated_user = True
    template_name = 'account/login.html'
    success_url = '/success_url/'
    success_message = "were successfully logged in."


def register(response):
    if response.user.is_authenticated:
        return redirect("blog:home")
    else:
        page = 'register_page'
        if response.method == "POST":
            form = RegistrationForm(response.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                form.save()
                messages.success(response, f'{username} has been created')
                return redirect("blog:home")
        else:
            form = RegistrationForm()

        return render(response, "account/register.html", {"form": form, 'page': page})


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile info has been updated')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html', context)


@login_required
def profile_view(request):
    profile = request.user.user_profile
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)
