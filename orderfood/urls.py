from django.urls import path
from orderfood.views import OrderFoodListView, OrderFoodDetailView, CategoryProductsView

urlpatterns = [
    path('orderfoods/', OrderFoodListView.as_view(), name='order-food'),
    path('orderfood/<int:pk>/', OrderFoodDetailView.as_view(), name='order-food'),
    path('category-food/<int:pk>/', CategoryProductsView.as_view(), name='category-foods')
]
