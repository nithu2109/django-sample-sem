from django.contrib import admin
from . models import Calorie
@admin.register(Calorie)

# Register your models here.
class Calorieadmin(admin.ModelAdmin):
    list_display=('foodid','fooditem','calorie')
    list_filter=('calorie','fooditem')
    ordering=('fooditem',)
