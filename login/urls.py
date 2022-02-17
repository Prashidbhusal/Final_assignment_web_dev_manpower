from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('login', views.login_user,name='login'),
    path("register", views.register_user),
    path('logout', views.logout_user),
    path('profile',views.user_account,name='useraccount')
]