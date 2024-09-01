from django.contrib import admin

from .models import Contact, Home, Suscribers

# Register your models here.


admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Suscribers)