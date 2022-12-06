from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Group

from CalorieCounter.accounts.forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserEditForm, \
    CustomUserDeleteForm
from CalorieCounter.accounts.models import CustomUser
from CalorieCounter.accounts.functionality import *


class UserRegisterView(views.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usr = form.save()
        user = CustomUser.objects.get(username=usr.username)
        set_user_info(user)
        if user.motivations_group:
            group = Group.objects.get(name='Motivations')
            group.user_set.add(user)
        return super().form_valid(form)


class UserLoginView(auth_views.LoginView):
    form_class = CustomUserLoginForm
    template_name = 'account/login.html'

    def get_success_url(self):
        user = CustomUser.objects.get(username=self.request.user.username)
        set_user_info(user)
        return reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class UserDetailsView(views.DetailView):
    model = CustomUser
    template_name = 'account/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class UserEditView(views.UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'account/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self, *args, **kwargs):
        user = CustomUser.objects.get(username=self.request.user.username)
        set_user_info(user)
        return reverse_lazy('profile details', kwargs={'username': self.object.username})


class UserDeleteView(views.DeleteView):
    model = CustomUser
    form_class = CustomUserDeleteForm
    template_name = 'account/profile_delete.html'

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.request.user.delete()
        return redirect('home')
