from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView


from django.views.generic import DeleteView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from accounts import forms
from accounts import models


def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            avatar = form.cleaned_data['avatar']
            user.save()
            account = models.Account(user=user, avatar=avatar)
            account.save()

            return redirect('login')
        else:
            return render(request, 'create_account.html', {'form': form})
    else:
        form = forms.UserRegisterForm()
        return render(request, 'create_account.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('index')
            else:
                return render(request, "login_account.html", {"message":"Invalid data"})

    form = AuthenticationForm()
    return render(request, 'login_account.html', {'form':form})


@login_required
def edit_profile(request):
    user = request.user
    model_profile, _ =models.Account.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = forms.UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('email'):
                user.email = data.get('email')
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            model_profile.avatar = data.get('avatar') if data.get('avatar') else model_profile.avatar

            model_profile.save()
            user.save()
            return redirect('index') 
        else:
            return render(request, "edit_account.html", {"form":form})

    form = forms.UserUpdateForm(
        initial={
            'email':user.email,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'avatar':model_profile.avatar,
        }
    )
    return render(request, "edit_account.html", {"form":form , "user":user, "avatar":model_profile.avatar})


class CustomLogoutView(LogoutView):
    template_name = 'logout_account.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect(reverse('index')) 


class DeleteAccount(LoginRequiredMixin, DeleteView):
    model = models.Account
    success_url = reverse_lazy('index')
    context_object_name = 'account'
    template_name = 'delete_account.html'
