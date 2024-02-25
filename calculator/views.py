from django.shortcuts import render

# Create your views here.

tax_rate = 0.15


def default_view(request):
    return render(request, 'index.html')


def calculate_tax(request, price):
    price = float(price)
    total = price + (price * tax_rate)
    return render(request, 'calculate_tax.html', {'total': total})


def tax_rate_view(request):
    return render(request, 'tax_rate.html', {'tax_rate': f'{tax_rate * 100}%'})