from django.contrib import admin
from myapp.models import Contact, Category, Team, Dish, Profile,Order

admin.site.site_header = "Arafat's Kitchen | Admin"

class ContactAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'added_on', 'is_approved']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']


admin.site.register(Contact, ContactAmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Team, TeamAdmin )
admin.site.register(Dish, DishAdmin )
admin.site.register(Profile)
admin.site.register(Order)