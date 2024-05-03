
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact_us,name="contact"),
    path('about/',views.about,name="about"),
    path('team/',views.team_members,name="team"),
    path('dishes/',views.all_dishes,name="all_dishes"),
    
]
