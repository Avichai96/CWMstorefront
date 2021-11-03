from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Q, F, Func, Value, ExpressionWrapper
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models.fields import DecimalField
from store.models import Customer, Product, OrderItem, Order


def say_hello(request):
    # Selecting field to query
    # queryset =Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # Deffering Fields
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # Selecting related objects
    # queryset =  Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # Aggregating Objects
    # result = Product.objects.filter(collection__id=3).aggregate(Min('unit_price'), Max('unit_price'), Avg('unit_price'))

    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )

    # Create Field to order_count in Customer Tabel
    # queryset = Customer.objects.annotate(
    #     order_count=Count('order')
    # )

    # Working with Expression Wrapper
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.aggregate(discounted_price=discounted_price)

    return render(request, 'hello.html', {'name': 'Avichai'})
