from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Products
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class FilterView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    search_fields = ('product_id', 'product_name')
    filter_fields = {
        'stock': ['gte', 'lte'],
    }

@csrf_exempt
def tokenlogin(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Wrong username or password!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            token = Token.objects.get(user=user).key
            print("Token:"+token)
        return JsonResponse({'token': str(token)}, status=HTTP_200_OK)



class ProductLists(APIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
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

class ProductView(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)