from django.urls import path
from category.views import CategoryListView, CategoryDetailView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]