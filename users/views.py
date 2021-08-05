from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse

from . import forms as users_forms
from . import models as users_models
from . import mixins as users_mixins

# Create your views here.

class LoginView(users_mixins.LoggedOutOnlyView, FormView):
    template_name = "users/login.html"
    form_class = users_forms.LoginForm   # () 없음에 주의
    # success_url = reverse_lazy("core:home")  # url을 부를때 생성
    
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))



class SignUpView(users_mixins.LoggedOutOnlyView, FormView):
    template_name = "users/signup.html"
    form_class = users_forms.SignUpForm
    success_url = reverse_lazy("core:home")

    # initial = {  # 폼에 들어갈 기본 데이터를 미리 입력
    #     "first_name": "Nicoas",
    #     "last_name": "Serr",
    #     "email": "itn@las.com",
    #     }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserProfileView(users_mixins.LoggedInOnlyView, DetailView):
    model = users_models.User
    context_object_name = "user_obj"  # 섞이면 안된다.   

class UpdateProfileView(users_mixins.LoggedInOnlyView, UpdateView):
    model = users_models.User
    template_name = "users/update-profile.html" # rlqhsrkqt user_form.html
    fields = (
        "first_name",
        "last_name",     
        "bio",
        "preference",
        "language",
        "fav_book_cat",
        "fav_movie_cat",
    )
        
    def get_object(self, queryset=None):
        return self.request.user

class UpdatePasswordView(users_mixins.LoggedInOnlyView, PasswordChangeView):
    
    template_name = "users/update-password.html"