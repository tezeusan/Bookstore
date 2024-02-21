from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Catalog",
        'content': 'The Book Heaven - Catalog',
        'description': 'Your literary haven for all things reading',
        "goods": [
            {"image": "images/goods/1.jpg",
             "name": "Tea Table and Three Chairs",
             "description": "Set of three chairs and a designer table for the living room.",
             "price": 150.00},

            {"image": "images/goods/2.jpg",
             "name": "Tea Table and Two Chairs",
             "description": "Set of a table and two chairs in a minimalist style.",
             "price": 93.00},

            {"image": "images/goods/3.jpg",
             "name": "Double Bed",
             "description": "Double bed with a headboard and overall very orthopedic.",
             "price": 670.00},

            {"image": "images/goods/4.jpg",
             "name": "Kitchen Table with Sink",
             "description": "Dining kitchen table with a built-in sink and chairs.",
             "price": 365.00},

            {"image": "images/goods/1.jpg",
             "name": "Kitchen Table with Built-in Appliances",
             "description": "Kitchen table with a built-in stove and sink. Many shelves and, in general, beautiful.",
             "price": 430.00},

            {"image": "images/goods/2.jpg",
             "name": "Corner Sofa for the Living Room",
             "description": "Corner sofa, unfolds into a double bed, perfect for the living room and entertaining guests!",
             "price": 610.00},

            {"image": "images/goods/3.jpg",
             "name": "Bedside Table",
             "description": "Bedside table with two drawers (flower not included in the set).",
             "price": 55.00},

            {"image": "images/goods/4.jpg",
             "name": "Ordinary Sofa",
             "description": "Sofa, also known as an ordinary couch, nothing remarkable to describe.",
             "price": 190.00},

            {"image": "images/goods/1.jpg",
             "name": "Office Chair",
             "description": "Office chair, described as great, but it's just a chair, what else can you say...",
             "price": 30.00},

            {"image": "images/goods/2.jpg",
             "name": "Plant",
             "description": "A plant to decorate your interior, bringing freshness and tranquility to the environment.",
             "price": 10.00},

            {"image": "images/goods/3.jpg",
             "name": "Stylized Flower",
             "description": "Designer flower (possibly artificial) for decorating the interior.",
             "price": 15.00},

            {"image": "images/goods/4.jpg",
             "name": "Unusual Bedside Table",
             "description": "A somewhat strange-looking table, but suitable for placement next to the bed.",
             "price": 25.00}
        ],

    }

    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
