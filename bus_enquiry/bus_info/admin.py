from django.contrib import admin

# Register your models here.
from .models import Bus

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display=("busid","bustype","source","destination","startingat","willreachat","stops","drivername","conductorname")