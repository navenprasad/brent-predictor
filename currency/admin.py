# from django.contrib import admin
#
# # Register your models here.
#
# # Register your models here.
# from .models import Currencies
#
# class CurrenciesAdmin(admin.ModelAdmin):
#     #list_display = ["__str__", "email","timestamp", "updated"]
#
#     class Meta:
#         model = Curencies
#
#
# admin.site.register(Currencies, CurrenciesAdmin)

from django.contrib import admin
from brent.currency.models import Currencies

admin.site.register(Currencies)
