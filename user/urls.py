from django import views
from django.urls import path
from . import views


urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("accounts/newest/<int:num>/", views.AccountsNewest.as_view()),
    path("accounts/<pk>/", views.UpdateAccount.as_view()),
    path("accounts/<pk>/management/", views.SoftDelete.as_view()),
]
