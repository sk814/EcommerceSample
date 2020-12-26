# serializers.py
from rest_framework import serializers
from .models import Products,Users


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = ('product_id', 'product_name', 'cost_price', 'created_date','selling_price','stock')

