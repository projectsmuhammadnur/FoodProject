from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from setuptools.command.install import install

from category.models import Category
from category.serializer import CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        instance = Category.objects.all()
        print(instance)
        serializer = CategorySerializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = CategorySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = CategorySerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
