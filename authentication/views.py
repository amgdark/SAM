from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

#Esta clase renderiza el log del sistma SAM.
class Login_view(LoginView):
	template_name = 'accounts/login.html'
	form_class = AuthenticationForm