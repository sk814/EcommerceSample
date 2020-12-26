from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ProductSerializer, UsersSerializer
from .models import Products, Users
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class Login(APIView):
    def post(self, request):
        print("POST DATA")
        print(request, request.data)
        try:
            user = Users.objects.get(username=request.data['username'],
                                     password=request.data['password'])
            if (user):
                return Response(request.data, status=status.HTTP_200_OK)
            else:
                return Response("NO USER FOUND", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("NO USER FOUND", status=status.HTTP_400_BAD_REQUEST)

class User(APIView):
    def get(self, request, format=None):
        products = Users.objects.all()
        serializer = UsersSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("POST DATA")
        print(request)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductLists(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        print ("POST DATA")
        print (request)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)