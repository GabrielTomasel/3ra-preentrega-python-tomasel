from django.urls import path
from accounts.views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', edit_profile, name='profile'),
    path("account_delete/<int:pk>", DeleteAccount.as_view(), name="delete_account"),
]