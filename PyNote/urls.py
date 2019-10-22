"""PyNote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entry_list/', entry_list_controller, name='entry_list'),
    path('register/', user_register_controller, name='register'),
    path('account/', account_controller, name='account'),
    path('change_password/', ChangePasswordController.as_view(), name='change_password'),
    path('password_change_done/', PasswordChangeDoneController.as_view(), name='password_change_done'),
    path('login/', LoginController.as_view(), name='login'),
    path('logout/', LogoutController.as_view(), name='logout'),
    path('', topic_list_controller, name='topic_list'),
    path('remove_topic/', remove_topic_controller, name='remove_topic')
]

