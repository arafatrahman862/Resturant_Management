
from django.contrib import admin
from django.urls import path, include
from myapp import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact_us,name="contact"),
    path('about/',views.about,name="about"),
    path('team/',views.team_members,name="team"),
    path('dishes/',views.All_dishes.as_view(),name="all_dishes"),
    path('register/',views.register,name="register"),
    path('login/', views.signin, name='login'),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    
]
