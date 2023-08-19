from django.urls import path
from orderfood.views import OrderFoodListView, OrderFoodDetailView

urlpatterns = [
    path('orderfoods/', OrderFoodListView, name='order-food'),
    path('orderfood/<int:pk>/', OrderFoodDetailView, name='order-food')
]
