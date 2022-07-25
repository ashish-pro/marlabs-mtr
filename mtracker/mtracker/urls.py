"""mtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('search/', views.search, name='search'),
    path('hr-profile/', views.profileData, name='profile'),
    path('feedback/', views.feedbackData, name='feedback'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register', views.user_registration, name='registration'),
    path('search/updatetask/<int:id>', views.updateTask, name='updatetask'),
    path('search/deletetask/<int:id>', views.deleteTask, name='deletetask'),
    path('search/searchresult/', views.searchResult, name='searchresult'),
    path('password-reset/',views.resetPassword, name='passwordreset'),
    path('changepass/<str:id>/',views.changePassword, name="changepassword"), 
   
]
