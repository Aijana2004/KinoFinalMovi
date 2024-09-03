from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_class = ProductFilter
        search_fields =['product_list']
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductPhotosViewSet(viewsets.ModelViewSet):
    queryset = ProductPhotos.objects.all()
    serializer_class = ProductPhotosSerializer



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer