from django.urls import path
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register",views.Regsiter.as_view()),
    path("logout",views.Logout.as_view()),
    path("login",obtain_auth_token)
]