from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceListing, Categoty
from .serializers import ServiceListingSerializer, CategorySerializer

# Create your views here.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'provider') and obj.provider == request.user
    

class ServiceListingViewSet(viewsets.ModelViewSet):
    queryset = ServiceListing.objects.filter(is_active=True).select_related('category', 'provider')
    serializer_class = ServiceListingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__id', 'town', 'suburb', 'provider__id']
    search_filter = ['title', 'description', 'provider__username']

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categoty.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]