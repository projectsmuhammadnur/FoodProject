from django.db import models


class RoleChoices(models.TextChoices):
    MALE = ("admin", "Admin")
    FEMALE = ("operator", "Operator")


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    role = models.CharField(max_length=8, choices=RoleChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.role} {self.firstname}"


class TelegramUsers(models.Model):
    chat_id = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    full_name = models.CharField(max_length=60)
    username = models.CharField(max_length=30)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"

    def __str__(self):
        return f"{self.chat_id} {self.is_blocked}"
