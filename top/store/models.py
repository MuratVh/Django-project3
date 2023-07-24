from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'catigories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField()
    is_discounted = models.BooleanField()
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('store.Brand', on_delete=models.CASCADE)
    image = models.ImageField(default='default-product-image.png', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_products')

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.pk}"


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    guest = models.ForeignKey(
        'store.Guest', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

    def total_price(self):
        return self.product.price * self.quantity


class Guest(models.Model):
    token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'guests'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    total_price = models.IntegerField()

    def __str__(self):
        return f"Заказ №{self.pk}"

    def order_products_list(self):
        return ', '.join([f'{order.product.name} {order.amount} шт'
                          for order in self.order_products.all()])


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_products'
    )
    # item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.product


RATE_CHOICES = [
    (5, 'Отлично'),
    (4, 'Хорошо'),
    (3, 'Нормально'),
    (2, 'Плохо'),
    (1, 'Ужасно'),
]


class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.customer.username} о {self.product.name}'
