from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product

# считаем общую сумму используя запрос в баззу даных(через БД)
def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity')) # aggregate - метод для агрегированых запросов в базе данных
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total.html', context)


# считаем общую сумму используя вью запрос
def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total.html', context)


# считаем общую сумму используя шаблон(шаблон должен обратиться к моделе)
def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'products': Product,
    }
    return render(request, 'myapp6/total.html', context)


# Create your views here.
