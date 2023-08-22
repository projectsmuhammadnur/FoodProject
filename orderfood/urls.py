from django.urls import path
from orderfood.views import OrderFoodListView, OrderFoodDetailView, CategoryProductsView

urlpatterns = [
    path('orderfoods/', OrderFoodListView, name='order-food'),
    path('orderfood/<int:pk>/', OrderFoodDetailView, name='order-food'),
    path('category-food/<int:pk>/', CategoryProductsView.as_view(), name='category-foods')
]
