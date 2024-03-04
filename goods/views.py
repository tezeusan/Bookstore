from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import Products


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 8)
    current_page = paginator.page(page)

    context = {
        "title": "Catalog",
        'content': 'The Book Heaven - Catalog',
        'description': 'Your literary haven for all things reading',
        "goods": current_page,
        "slug_url": category_slug,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
