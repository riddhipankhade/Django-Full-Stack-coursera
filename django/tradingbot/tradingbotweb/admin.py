from django.contrib import admin
from .models import Currency, Transection, CurrencyHistory

class TransectionAdmin(admin.ModelAdmin):
    readonly_fields = ('exchange_date',)
class currencyHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at',)
# Register your models here.
from .models import Currency, Transection
admin.site.register(Currency)
admin.site.register(Transection,TransectionAdmin)
admin.site.register(CurrencyHistory,currencyHistoryAdmin)
admin.site.register(ExchangeGoal,currencyHistoryAdmin)
