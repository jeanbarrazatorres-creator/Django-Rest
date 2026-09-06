from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .serializers import InventorySerializer
from .models import Inventory 


class AddtoInventory(APIView):
    def post(self, request):
        serializer = InventorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

class ReadInventory(APIView):
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many = True)
        return Response(serializer.data, status = 200)

class UpdateInventory(APIView):
    def put(self, request, pk):
        inventory = Inventory.objects.get(pk = pk)
        serializer = InventorySerializer(inventory, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.error_messages, status = 400)

class DeleteInventory(APIView):
    def delete(self, request, pk):
        inventory = Inventory.objects.get(pk = pk)
        inventory.delete()
        return Response(status = 204)

    