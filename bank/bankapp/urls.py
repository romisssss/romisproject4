from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('userhome/', views.userhome, name='userhome'),
    path('register/', views.register, name='register'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('userform/', views.userform, name='userform'),
    path('register_user/',views.register_user,name='register_user'),
    path('success/', views.success, name='success'),
    path('get_branches/<int:district_id>/', views.get_branches, name='get_branches'),
    path('logout',views.logout,name='logout'),
]