from django.shortcuts import render
from tradingbotweb.models import Currency, Transection, CurrencyHistory, CurrencyBalance, ExchangeGoal


# Create your views here.
def index(request):
    last_balance = CurrencyBalance.objects.last()
    exchange_goal = last_balance.exchange_goal.first()

    context = {
        'last_balance': last_balance,
        'exchange_goal': exchange_goal,
    }

    return render(request, 'Home.html', context)