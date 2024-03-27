from django.db import models
from django.urls import reverse


class Authors(models.Model):
    author = models.CharField(max_length=150, blank=True, null=True, default='', verbose_name='Author')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Author Slug')

    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.author


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ("id",)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    author = models.ForeignKey(to=Authors, on_delete=models.CASCADE, verbose_name='Author')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Image")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Price")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Discount")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Category")

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.name} Quantity - {self.quantity}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
