import tushare as ts
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'stock_market/home.html')


def avg(request):
    all_data = ts.get_index().iterrows()
    data = {
        'message': 'Hello World!',
        'title': '股市大盘',
        'all_data': all_data,
    }
    return render(request, 'stock_market/avg.html', data)
