from django.urls import path

from user.views import UserList, UserDetail, TelegramUserDetail, TelegramUserList

urlpatterns = [
    path('users/', UserList.as_view(), name='users-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('telegram-users/', TelegramUserList.as_view(), name='users-list'),
    path('telegram-user/<str:pk>/', TelegramUserDetail.as_view(), name='user-detail'),
]
