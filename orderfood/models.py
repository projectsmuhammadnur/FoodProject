from django.db import models

from category.models import Category
from user.models import TelegramUsers, User


class Food(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=125)
    price = models.IntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, related_name='category-food', on_delete=models.CASCADE)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return self.name


class Order(models.Model):
    total_price = models.IntegerField()
    lat = models.IntegerField()
    lon = models.IntegerField()
    description = models.TextField(max_length=500)
    telegram_user = models.ForeignKey(TelegramUsers,
                                      related_name='order-telegram-user',
                                      on_delete=models.CASCADE)
    deliver_by = models.ForeignKey(User, related_name='order-user', on_delete=models.CASCADE)
    status = models.BooleanField()
    order_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.total_price


class OrderFood(models.Model):
    order = models.ForeignKey(Order, related_name='orderfood', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='orderfood', on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'OrderFood'
        verbose_name_plural = 'OrderFoods'

    def __str__(self):
        return self.food.name
