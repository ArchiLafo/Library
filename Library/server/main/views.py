from django.shortcuts import render
from products.models import ProductCategory, Product


def main(request):
    return render(
        request,
        'main/index.html',
        {
            'title': 'Книжная полка',
            'menu': ProductCategory.objects.all(),
            'obj': Product.objects.all(),
        }
    )
