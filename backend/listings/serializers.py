from rest_framework import serializers
from .models import Category, ServiceListing
from accounts.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceListingSerializer(serializers.ModelField):
    model = ServiceListing
    fields = '__all__'
    read_only_fields = ('provider', 'created_at', 'updated_at')