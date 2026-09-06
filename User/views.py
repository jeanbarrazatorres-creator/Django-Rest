from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import UserSerializer 
from django.contrib.auth import authenticate 
from .models import User 

class AddtoUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

class LoginUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username = username, password = password)

        if user is not None: 
            return Response({"message": "login existoso", "username": user.username}, status = 200)
        return Response({"error": "user or password incorrectos"}, status = 401)

class DeleteUser(APIView):
    def delete(self, request, pk):
         user = User.objects.get(pk = pk)
         user.delete()
         return Response({"message": "usiario eliminado"}, status = 200)