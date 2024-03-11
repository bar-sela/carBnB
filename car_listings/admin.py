from django.contrib import admin
from .models import Car, Person, Rent

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Rent)