from django.contrib import admin
from .models import Pizaa,Burger,Drinks
# Register your models here.
class PizaaAdmin(admin.ModelAdmin):
    list_display = ('name','priceM','priceL','pImage')

class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name','priceM','priceL','bImage']

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name','priceM','priceL','dImage')

admin.site.register(Pizaa,PizaaAdmin)
admin.site.register(Burger,BurgerAdmin)
admin.site.register(Drinks,DrinkAdmin)