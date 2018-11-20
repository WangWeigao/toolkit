from django.shortcuts import render
from django.http import HttpResponse
import tushare as ts

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def avg(request):
    all_data = ts.get_index().iterrows()
    data = {
            'message': 'Hello World!',
            'title': '股市大盘',
            'all_data': all_data,
            }
    return render(request, 'stock_market/avg.html', data)
