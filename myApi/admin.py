from django.contrib import admin
from .models import Country, State, Town, City, Person
# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Town)
admin.site.register(City)
admin.site.register(Person)