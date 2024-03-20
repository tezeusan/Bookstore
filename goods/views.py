from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from goods.models import Products
from goods.utils import q_search
from django.http import Http404


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', 'id')
    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        # Вместо get_list_or_404 используйте filter и проверьте, не пустой ли QuerySet
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404("No Products found.")
    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

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
