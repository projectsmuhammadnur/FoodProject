from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User, TelegramUsers
from user.serializers import UsersSerializer, TelegramUsersSerializer


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get_instance(self, pk):
        try:
            instance = User.objects.get(pk=pk)
            return instance
        except User.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_instance(pk=kwargs.get('pk'))
        serializer = UsersSerializer(instance, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_instance(pk=kwargs.get('pk'))
        serializer = UsersSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_instance(pk=kwargs.get('pk'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TelegramUserList(APIView):
    def get(self, request, *args, **kwargs):
        queryset = TelegramUsers.objects.all()
        serializer = TelegramUsersSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TelegramUsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class TelegramUserDetail(APIView):
    def get_instance(self, pk):
        try:
            instance = TelegramUsers.objects.get(chat_id=pk)
            return instance
        except User.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_instance(pk=kwargs.get('pk'))
        serializer = TelegramUsersSerializer(instance, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_instance(pk=kwargs.get('pk'))
        serializer = TelegramUsersSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_instance(pk=kwargs.get('pk'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
