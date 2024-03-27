from django.contrib import admin

from goods.models import Categories, Products, Authors


# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['quantity', 'price', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = ['name', 'category', 'slug', 'description', 'image', ("price", "discount"), 'quantity', ]


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('author',)}
    list_display = ['author', ]
