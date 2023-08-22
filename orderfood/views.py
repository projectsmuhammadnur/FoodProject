from rest_framework.response import Response
from rest_framework.views import APIView
from orderfood.models import OrderFood, Food
from rest_framework.exceptions import NotFound
from orderfood.serializer import OrderFoodSerializer, FoodSerializer
from rest_framework import status


class OrderFoodListView(APIView):
    def get(self, request):
        instance = OrderFood.objects.all()
        serializer = OrderFoodSerializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderFoodSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderFoodDetailView(APIView):
    def get_object(self, pk):
        try:
            return OrderFood.objects.get(pk=pk)
        except OrderFood.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(kwargs.get("pk"))
        serializer = OrderFoodSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(kwargs.get("pk"))
        serializer = OrderFoodSerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryProductsView(APIView):
    def get(self, request, *args, **kwargs):
        instance = Food.objects.filter(category=kwargs.get("pk"))
        serializer = FoodSerializer(instance, many=True)
        return Response(serializer.data)
