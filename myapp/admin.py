from django.contrib import admin
from myapp.models import Contact

admin.site.site_header = "Arafat's Kitchen | Admin"

admin.site.register(Contact)