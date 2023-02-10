from django.contrib import admin
from .models import Boat

# Register your models here.

class BoatAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

admin.site.register(Boat, BoatAdmin)