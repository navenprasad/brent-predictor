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
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "prediction", "technique"]

admin.site.register(Currency, CurrencyAdmin)
admin.site.site_header = 'Brent Predictor - Naven Prasad (FYP 2016)'
