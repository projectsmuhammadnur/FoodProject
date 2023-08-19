from django.contrib import admin

from user.models import User, TelegramUsers

admin.site.register(User)
admin.site.register(TelegramUsers)
