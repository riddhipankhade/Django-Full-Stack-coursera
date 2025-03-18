from django.db import models
from django.core.validators import MinValueValidator
import decimal, json
import requests

# Create your models here.
class Currency(models.Model):
    symbol = models.CharField(max_length=10,primary_key=True)
    usd_value = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)

class Transection(models.Model):
    orignal_currency         = models.ForeignKey(Currency, on_delete=models.CASCADE)
    destination_currency     = models.ForeignKey(Currency, on_delete=models.CASCADE)
    orignal_currency         = models.DecimalField(max_digits=10, decimal_places=2)
    destination_currency     = models.DecimalField(max_digits=10, decimal_places=2)
    commission               = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    exchange_date            = models.DateTimeField(auto_now_add=True)

class CurrencyHistory(models.Model):
    symbol = models.ForeignKey(Currency, on_delete=models.CASCADE)
    usd_value = models.DecimalField(max_digits=10, decimal_places=6, default=1.0)
    create_at = models.DateTimeField(auto_now_add=True)

def save(self, *args, **kwargs):
    self.usd_value = self.get_value()
    super(CurrencyHistory, self).save(*args, **kwargs)

def get_value(self):
    app_url=f"https://economia.awesomeapi.com.br/json/all/{self.symbol.symbol},USD"
    response = requests.get(app_url).content
    json_data = json.loads(response)
    usd_ask_value = json_data[self.symbol.symbol]['ask']
    print(f"USD Ask Value: {usd_ask_value}")
    decimal_value = decimal.Decimal(usd_ask_value)
    return decimal_value

class CurrencyBalance(models.Model):
    currency=models.ForeignKey(Currency, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    share_partfolio = models.IntegerField(places=2,default=0,validators=[MinValueValidator(0)])
    value=models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

class ExchangeGoal(models.model):
    origin_balance = models.ForeignKey(CurrencyBalance, on_delete=models.CASCADE, related_name='exchange_goal')
    destination_currency = models.ForeignKey(CurrencyBalance, on_delete=models.CASCADE, related_name='exchange_goal')
    initial_value = models.DecimalField(max_digits=10, decimal_places=2)
    threshold = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    excuted_at = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    transaction = models.ForeignKey(Transection, on_delete=models.CASCADE, null=True, blank=True)
    