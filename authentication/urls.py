from django.urls import path
from .views import Login_view
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('login/', Login_view.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
