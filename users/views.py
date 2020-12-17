from django.shortcuts import render

# Create your views here.
# Django
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import FormView, UpdateView

from users.models import Profile

from users.forms import SignupForm


class LoginView(auth_views.LoginView):

    """Class based Login View."""
    template_name = 'users/login.html'


class SignUpView(FormView):
    """Users sign up view."""
    model = Profile
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['type']

    def get_object(self, queryset=None):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        # return reverse('home', kwargs={'username': username})
        return reverse('home')


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html' # This view is never rendered bc it goes straight to the redirected url
