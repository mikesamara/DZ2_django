from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)  # описание, blank=True обязательное или нет(не обязательное)
    price = models.DecimalField(default=999999.99, max_digits=8,
                                decimal_places=2)  # стоимость, max_digits максимальное кол-во цифр
    quantity = models.PositiveSmallIntegerField(
        default=0)  # кол-во PositiveSmallIntegerField - положительное число, не допускает отрицательные числа, small хранение в байтах
    date_add = models.DateTimeField(auto_now_add=True)  # дата добавление,  auto_now_add поле заполняется автомотически
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)  # рейтинг

    def __str__(self):
        return self.name

    @property
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all())
# Create your models here.
